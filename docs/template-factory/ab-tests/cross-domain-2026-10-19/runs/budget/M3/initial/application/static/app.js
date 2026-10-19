/* 个人月度预算：前端逻辑。与 JSON API 共用同一真实状态。 */
(function () {
  "use strict";

  var API = window.APP_API || {};
  var state = { month: null, categories: [], transactions: [], totals: {} };
  var editingTxnId = null;

  function $(id) { return document.getElementById(id); }

  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) { node.className = cls; }
    if (text !== undefined && text !== null) { node.textContent = text; }
    return node;
  }

  function pad2(n) { return (n < 10 ? "0" : "") + n; }

  function currentMonth() {
    var d = new Date();
    return d.getFullYear() + "-" + pad2(d.getMonth() + 1);
  }

  function feedback(message, kind) {
    var box = $("feedback");
    box.className = "feedback" + (kind ? " " + kind : "");
    box.textContent = message || "";
  }

  function apiFetch(path, options) {
    return fetch(path, options).then(function (resp) {
      return resp.text().then(function (text) {
        var data = null;
        try { data = text ? JSON.parse(text) : null; } catch (e) { data = null; }
        if (!resp.ok) {
          var msg = (data && data.error) ? data.error : ("请求失败（HTTP " + resp.status + "）");
          throw new Error(msg);
        }
        return data;
      });
    });
  }

  function jsonOptions(method, payload) {
    return {
      method: method,
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(payload)
    };
  }

  function loadState() {
    var month = $("month").value || currentMonth();
    $("month").value = month;
    return apiFetch(API.state + "?month=" + encodeURIComponent(month),
                    { headers: { "Accept": "application/json" } })
      .then(function (data) {
        state = data;
        render();
        feedback("");
      })
      .catch(function (err) { feedback("加载失败：" + err.message, "error"); });
  }

  function render() {
    renderTotals();
    renderCategories();
    renderTransactions();
    renderCategoryOptions();
  }

  function renderTotals() {
    var t = state.totals || {};
    var box = $("totals");
    box.textContent = "";
    box.appendChild(el("span", "total", "本月计划 " + (t.budget || "0.00")));
    box.appendChild(el("span", "total", "已花 " + (t.spent || "0.00")));
    var remaining = el("span", "total", "剩余 " + (t.remaining || "0.00"));
    if ((t.remaining || "").charAt(0) === "-") { remaining.classList.add("negative"); }
    box.appendChild(remaining);
  }

  function emptyRow(tbody, colspan, text) {
    var tr = el("tr");
    var td = el("td", "empty", text);
    td.colSpan = colspan;
    tr.appendChild(td);
    tbody.appendChild(tr);
  }

  function renderCategories() {
    var tbody = $("category-rows");
    tbody.textContent = "";
    var cats = state.categories || [];
    if (!cats.length) {
      emptyRow(tbody, 5, "本月还没有分类，请先建立分类与预算。未使用分类会一直显示。");
      return;
    }
    cats.forEach(function (cat) {
      var tr = el("tr");
      tr.appendChild(el("td", null, cat.name));
      tr.appendChild(el("td", "num", cat.budget));
      tr.appendChild(el("td", "num", cat.spent));
      var remaining = el("td", "num", cat.remaining);
      if (cat.remaining.charAt(0) === "-") { remaining.classList.add("negative"); }
      tr.appendChild(remaining);
      var action = el("td");
      var button = el("button", "link", "改预算");
      button.type = "button";
      button.addEventListener("click", function () { editBudget(cat); });
      action.appendChild(button);
      tr.appendChild(action);
      tbody.appendChild(tr);
    });
  }

  function renderTransactions() {
    var tbody = $("transaction-rows");
    tbody.textContent = "";
    var txns = state.transactions || [];
    if (!txns.length) {
      emptyRow(tbody, 5, "本月还没有支出记录。");
      return;
    }
    var nameById = {};
    (state.categories || []).forEach(function (cat) { nameById[cat.id] = cat.name; });
    txns.forEach(function (txn) {
      var tr = el("tr");
      tr.appendChild(el("td", null, txn.date));
      tr.appendChild(el("td", null, nameById[txn.category_id] || ("#" + txn.category_id)));
      tr.appendChild(el("td", "num", txn.amount));
      tr.appendChild(el("td", "note", txn.note));
      var action = el("td");
      var edit = el("button", "link", "修改");
      edit.type = "button";
      edit.addEventListener("click", function () { beginEdit(txn); });
      var remove = el("button", "link danger", "删除");
      remove.type = "button";
      remove.addEventListener("click", function () { removeTransaction(txn); });
      action.appendChild(edit);
      action.appendChild(remove);
      tr.appendChild(action);
      tbody.appendChild(tr);
    });
  }

  function renderCategoryOptions() {
    var select = $("expense-category");
    var previous = select.value;
    select.textContent = "";
    var cats = state.categories || [];
    if (!cats.length) {
      var option = el("option", null, "（请先建立分类）");
      option.value = "";
      select.appendChild(option);
      return;
    }
    cats.forEach(function (cat) {
      var option = el("option", null, cat.name + "（剩余 " + cat.remaining + "）");
      option.value = String(cat.id);
      select.appendChild(option);
    });
    if (previous && select.querySelector('option[value="' + previous + '"]')) {
      select.value = previous;
    }
  }

  function saveCategory() {
    var name = $("category-name").value;
    if (!name.trim()) { feedback("请输入分类名称", "error"); return; }
    apiFetch(API.categories, jsonOptions("POST", {
      month: $("month").value,
      name: name,
      budget: $("category-budget").value
    })).then(function () {
      $("category-name").value = "";
      $("category-budget").value = "";
      feedback("分类已保存", "ok");
      return loadState();
    }).catch(function (err) { feedback("保存分类失败：" + err.message, "error"); });
  }

  function beginEdit(txn) {
    editingTxnId = txn.id;
    $("expense-date").value = txn.date;
    $("expense-category").value = String(txn.category_id);
    $("expense-amount").value = txn.amount;
    $("expense-note").value = txn.note;
    $("expense-save").textContent = "保存修改";
    feedback("正在修改支出 #" + txn.id + "，点击“保存修改”生效", "");
  }

  function resetExpenseForm() {
    editingTxnId = null;
    $("expense-amount").value = "";
    $("expense-note").value = "";
    $("expense-save").textContent = "记一笔";
  }

  function saveExpense() {
    var date = $("expense-date").value;
    var categoryId = parseInt($("expense-category").value, 10);
    if (!date) { feedback("请选择支出日期", "error"); return; }
    if (!categoryId) { feedback("请先建立并选择分类", "error"); return; }
    var payload = {
      date: date,
      category_id: categoryId,
      amount: $("expense-amount").value,
      note: $("expense-note").value
    };
    var url = editingTxnId ? (API.transactions + "/" + editingTxnId) : API.transactions;
    var method = editingTxnId ? "PUT" : "POST";
    apiFetch(url, jsonOptions(method, payload)).then(function () {
      feedback(editingTxnId ? "支出已更新" : "支出已记录", "ok");
      resetExpenseForm();
      return loadState();
    }).catch(function (err) { feedback("记录支出失败：" + err.message, "error"); });
  }

  function editBudget(cat) {
    var input = window.prompt("输入「" + cat.name + "」的新预算（元，两位小数）：", cat.budget);
    if (input === null) { return; }
    apiFetch(API.categories + "/" + cat.id, jsonOptions("PUT", { budget: input }))
      .then(function () { feedback("预算已更新", "ok"); return loadState(); })
      .catch(function (err) { feedback("更新预算失败：" + err.message, "error"); });
  }

  function removeTransaction(txn) {
    if (!window.confirm("确定删除这笔支出（" + txn.date + " " + txn.amount + " 元）？")) {
      return;
    }
    apiFetch(API.transactions + "/" + txn.id, { method: "DELETE" })
      .then(function () { feedback("支出已删除", "ok"); return loadState(); })
      .catch(function (err) { feedback("删除失败：" + err.message, "error"); });
  }

  function exportCsv() {
    var month = $("month").value || currentMonth();
    window.location.href = API.export + "?month=" + encodeURIComponent(month);
    feedback("正在导出 " + month + " 的 CSV…", "ok");
  }

  function onMonthChange() {
    resetExpenseForm();
    var month = $("month").value;
    if (month) { $("expense-date").value = month + "-01"; }
    loadState();
  }

  function init() {
    var monthInput = $("month");
    monthInput.value = currentMonth();
    $("expense-date").value = monthInput.value + "-01";
    monthInput.addEventListener("change", onMonthChange);
    $("category-save").addEventListener("click", saveCategory);
    $("expense-save").addEventListener("click", saveExpense);
    $("export-btn").addEventListener("click", exportCsv);
    loadState();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
