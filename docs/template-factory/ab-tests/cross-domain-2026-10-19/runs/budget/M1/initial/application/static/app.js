/* Browser UI for the local monthly budget app. Talks to the JSON API only. */
(function () {
  "use strict";

  var state = {
    month: "",
    categories: [],
    transactions: [],
    totals: { budget: "0.00", spent: "0.00", remaining: "0.00" }
  };
  var editingId = null;
  var requestedMonth = null;

  function $(id) { return document.getElementById(id); }

  function feedback(message, isError) {
    var box = $("feedback");
    box.textContent = message || "";
    box.classList.toggle("error", !!isError);
    box.classList.toggle("ok", !isError && !!message);
  }

  function cell(text) {
    var td = document.createElement("td");
    td.textContent = text;
    return td;
  }

  function api(path, options) {
    return fetch(path, options).then(function (res) {
      return res.text().then(function (text) {
        var data = null;
        if (text) {
          try { data = JSON.parse(text); } catch (err) { data = null; }
        }
        if (!res.ok) {
          var msg = (data && data.error) ? data.error : ("请求失败 (" + res.status + ")");
          throw new Error(msg);
        }
        return data;
      });
    });
  }

  function jsonOptions(method, payload) {
    return {
      method: method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    };
  }

  function currentMonth() {
    var now = new Date();
    var m = now.getMonth() + 1;
    return now.getFullYear() + "-" + (m < 10 ? "0" + m : "" + m);
  }

  // -- data ---------------------------------------------------------------

  function loadState() {
    var month = $("month").value || currentMonth();
    requestedMonth = month;
    return api("/api/state?month=" + encodeURIComponent(month)).then(function (data) {
      state = data;
      render();
    });
  }

  function render() {
    renderCategories();
    renderTransactions();
    renderCategoryOptions();
    $("totals").textContent =
      "计划 ¥" + state.totals.budget +
      " / 已花 ¥" + state.totals.spent +
      " / 剩余 ¥" + state.totals.remaining;
  }

  function renderCategories() {
    var tbody = $("category-rows");
    tbody.innerHTML = "";
    state.categories.forEach(function (cat) {
      var tr = document.createElement("tr");
      tr.appendChild(cell(cat.name));
      tr.appendChild(cell(cat.budget));
      tr.appendChild(cell(cat.spent));
      var remaining = cell(cat.remaining);
      if (cat.remaining.charAt(0) === "-") { remaining.className = "over"; }
      tr.appendChild(remaining);

      var actions = document.createElement("td");
      var input = document.createElement("input");
      input.type = "text";
      input.className = "budget-input";
      input.value = cat.budget;
      input.setAttribute("aria-label", cat.name + " 预算");
      var save = document.createElement("button");
      save.type = "button";
      save.className = "secondary";
      save.textContent = "保存";
      save.addEventListener("click", function () { saveBudget(cat.id, input.value); });
      actions.appendChild(input);
      actions.appendChild(save);
      tr.appendChild(actions);
      tbody.appendChild(tr);
    });
  }

  function renderTransactions() {
    var tbody = $("transaction-rows");
    tbody.innerHTML = "";
    var names = {};
    state.categories.forEach(function (c) { names[c.id] = c.name; });
    state.transactions.forEach(function (txn) {
      var tr = document.createElement("tr");
      tr.appendChild(cell(txn.date));
      tr.appendChild(cell(names[txn.category_id] || ""));
      tr.appendChild(cell(txn.amount));
      tr.appendChild(cell(txn.note));

      var actions = document.createElement("td");
      var edit = document.createElement("button");
      edit.type = "button";
      edit.className = "secondary";
      edit.textContent = "编辑";
      edit.addEventListener("click", function () { startEdit(txn); });
      var del = document.createElement("button");
      del.type = "button";
      del.className = "secondary";
      del.textContent = "删除";
      del.addEventListener("click", function () { deleteTransaction(txn.id); });
      actions.appendChild(edit);
      actions.appendChild(del);
      tr.appendChild(actions);
      tbody.appendChild(tr);
    });
    $("transaction-empty").hidden = state.transactions.length > 0;
  }

  function renderCategoryOptions() {
    var select = $("expense-category");
    var previous = select.value;
    select.innerHTML = "";
    state.categories.forEach(function (cat) {
      var opt = document.createElement("option");
      opt.value = String(cat.id);
      opt.textContent = cat.name;
      select.appendChild(opt);
    });
    if (previous && select.querySelector('option[value="' + previous + '"]')) {
      select.value = previous;
    }
  }

  // -- actions ------------------------------------------------------------

  function saveCategory() {
    var month = $("month").value;
    var name = $("category-name").value.trim();
    var budget = $("category-budget").value.trim();
    if (!month) { feedback("请先选择月份", true); return; }
    if (!name) { feedback("请输入分类名称", true); return; }
    if (budget === "") { feedback("请输入预算金额", true); return; }
    api("/api/categories", jsonOptions("POST", { month: month, name: name, budget: budget }))
      .then(function (created) {
        $("category-name").value = "";
        $("category-budget").value = "";
        return loadState().then(function () {
          if (created && created.id != null) {
            $("expense-category").value = String(created.id);
          }
          feedback("已保存分类「" + name + "」", false);
        });
      })
      .catch(function (err) { feedback(err.message, true); });
  }

  function saveBudget(id, value) {
    api("/api/categories/" + id, jsonOptions("PUT", { budget: String(value).trim() }))
      .then(function () { return loadState(); })
      .then(function () { feedback("预算已更新", false); })
      .catch(function (err) { feedback(err.message, true); });
  }

  function startEdit(txn) {
    editingId = txn.id;
    $("expense-date").value = txn.date;
    $("expense-category").value = String(txn.category_id);
    $("expense-amount").value = txn.amount;
    $("expense-note").value = txn.note;
    $("expense-save").textContent = "保存修改";
    $("expense-cancel").hidden = false;
    feedback("正在修改支出 #" + txn.id, false);
  }

  function cancelEdit() {
    editingId = null;
    $("expense-save").textContent = "保存支出";
    $("expense-cancel").hidden = true;
  }

  function saveExpense() {
    var date = $("expense-date").value;
    var categoryId = $("expense-category").value;
    var amount = $("expense-amount").value.trim();
    var note = $("expense-note").value;
    if (!date) { feedback("请选择支出日期", true); return; }
    if (!categoryId) { feedback("请先建立并选择分类", true); return; }
    if (amount === "") { feedback("请输入支出金额", true); return; }

    var payload = { date: date, category_id: Number(categoryId), amount: amount, note: note };
    var request = (editingId === null)
      ? api("/api/transactions", jsonOptions("POST", payload))
      : api("/api/transactions/" + editingId, jsonOptions("PUT", payload));

    request.then(function () {
      var wasEditing = editingId !== null;
      cancelEdit();
      $("expense-amount").value = "";
      $("expense-note").value = "";
      return loadState().then(function () {
        feedback(wasEditing ? "支出已更新" : "支出已记录", false);
      });
    }).catch(function (err) { feedback(err.message, true); });
  }

  function deleteTransaction(id) {
    api("/api/transactions/" + id, { method: "DELETE" })
      .then(function () { return loadState(); })
      .then(function () { feedback("支出已删除", false); })
      .catch(function (err) { feedback(err.message, true); });
  }

  function exportCsv() {
    var month = $("month").value;
    if (!month) { feedback("请先选择月份", true); return; }
    var link = document.createElement("a");
    link.href = "/api/export?month=" + encodeURIComponent(month);
    link.download = "budget-" + month + ".csv";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    feedback("已导出 " + month + " 的 CSV", false);
  }

  function onMonthChanged() {
    var month = $("month").value;
    if (!month || month === requestedMonth) { return; }
    cancelEdit();
    loadState().catch(function (err) { feedback(err.message, true); });
  }

  // -- init ---------------------------------------------------------------

  function init() {
    $("month").value = currentMonth();
    $("month").addEventListener("input", onMonthChanged);
    $("month").addEventListener("change", onMonthChanged);
    $("category-save").addEventListener("click", saveCategory);
    $("expense-save").addEventListener("click", saveExpense);
    $("expense-cancel").addEventListener("click", function () {
      cancelEdit();
      feedback("已取消修改", false);
    });
    $("export-btn").addEventListener("click", exportCsv);
    loadState().catch(function (err) { feedback(err.message, true); });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
