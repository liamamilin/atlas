// 渐进增强：归类删除对话框、确认门禁、排序自动提交。
// 服务端独立校验所有确认参数；这里的脚本只负责本地交互与错误提示。
(function () {
  "use strict";

  function byTestId(id) {
    return document.querySelector('[data-testid="' + id + '"]');
  }

  function text(el, value) {
    if (!el) return;
    el.textContent = value || "";
  }

  function categoryEntries() {
    var links = document.querySelectorAll('a[data-testid="category-link"]');
    var entries = [];
    for (var i = 0; i < links.length; i += 1) {
      entries.push({
        id: links[i].getAttribute("data-category-id") || "",
        name: (links[i].textContent || "").trim(),
      });
    }
    return entries;
  }

  function setDialogError(message) {
    text(byTestId("dialog-error"), message);
  }

  function setFormError(message) {
    text(byTestId("form-error"), message);
  }

  function openDialog(categoryId) {
    var dialog = byTestId("category-delete-dialog");
    if (!dialog) return;
    var base = dialog.getAttribute("data-base-path") || "";
    var action = base + "/categories/" + categoryId + "/delete";
    var forms = dialog.querySelectorAll("form");
    for (var i = 0; i < forms.length; i += 1) {
      forms[i].setAttribute("action", action);
    }
    var select = dialog.querySelector('select[name="targetCategoryId"]');
    if (select) {
      var entries = categoryEntries();
      select.innerHTML = "";
      for (var j = 0; j < entries.length; j += 1) {
        if (entries[j].id === String(categoryId)) continue;
        var option = document.createElement("option");
        option.value = entries[j].id;
        option.textContent = entries[j].name;
        select.appendChild(option);
      }
    }
    var confirmBox = dialog.querySelector('[data-testid="confirm-purge"]');
    if (confirmBox) confirmBox.checked = false;
    setDialogError("");
    dialog.hidden = false;
    dialog.classList.add("open");
  }

  function closeDialog() {
    var dialog = byTestId("category-delete-dialog");
    if (!dialog) return;
    setDialogError("");
    dialog.hidden = true;
    dialog.classList.remove("open");
  }

  document.addEventListener("click", function (event) {
    var target = event.target;
    if (!target || !target.closest) return;

    var deleteButton = target.closest('button[data-testid="category-delete"]');
    if (deleteButton) {
      openDialog(deleteButton.getAttribute("data-category-id"));
      return;
    }
    if (target.closest('button[data-testid="delete-cancel"]')) {
      closeDialog();
      return;
    }
    var purge = target.closest('button[data-testid="delete-purge"]');
    if (purge) {
      var dialog = byTestId("category-delete-dialog");
      var confirmBox = dialog ? dialog.querySelector('[data-testid="confirm-purge"]') : null;
      if (!confirmBox || !confirmBox.checked) {
        event.preventDefault();
        setDialogError("请先勾选确认，才能永久删除该归类中的记录。");
      } else {
        setDialogError("");
      }
      return;
    }
    var trashDelete = target.closest('button[data-testid="trash-delete-submit"]');
    if (trashDelete) {
      var form = trashDelete.closest("form");
      var box = form ? form.querySelector('[data-testid="trash-delete-confirm"]') : null;
      if (!box || !box.checked) {
        event.preventDefault();
        setFormError("请先勾选确认，才能永久删除这条记录。");
      } else {
        setFormError("");
      }
      return;
    }
    var clearButton = target.closest('button[data-testid="trash-clear-submit"]');
    if (clearButton) {
      var clearForm = clearButton.closest("form");
      var clearBox = clearForm ? clearForm.querySelector('[data-testid="trash-clear-confirm"]') : null;
      if (!clearBox || !clearBox.checked) {
        event.preventDefault();
        setFormError("请先勾选确认，才能清空回收站。");
      } else {
        setFormError("");
      }
    }
  });

  document.addEventListener("change", function (event) {
    var select = event.target;
    if (select && select.matches && select.matches('select[data-testid="sort-select"]')) {
      var form = select.closest("form");
      if (form) form.submit();
    }
  });
})();
