/* 生活待购与灵感收藏夹 —— 前端逻辑（原生 JS，无外部依赖） */
(function () {
  "use strict";

  var state = {
    categories: [],
    defaultCategoryId: null,
    bookmarks: [],
    currentCategory: null, // null 表示查看全部
    query: "",
    newestFirst: true,
    stats: { total: 0, opened: 0 }
  };

  var el = {};

  function $(id) { return document.getElementById(id); }

  function cache() {
    [
      "search-input", "search-clear", "toast", "add-form", "url-input", "title-input",
      "category-select", "note-input", "category-list", "category-form", "category-name",
      "total-count", "list-title", "list-hint", "bookmark-list", "empty-state",
      "sort-toggle", "stats-line", "edit-dialog", "edit-form", "edit-id", "edit-url",
      "edit-title", "edit-note", "edit-category", "edit-hint", "edit-cancel"
    ].forEach(function (id) {
      el[id] = $(id);
    });
  }

  function api(method, path, body) {
    var options = { method: method, headers: {} };
    if (body !== undefined) {
      options.headers["Content-Type"] = "application/json";
      options.body = JSON.stringify(body);
    }
    return fetch(path, options).then(function (response) {
      return response.json().catch(function () { return {}; }).then(function (data) {
        if (!response.ok) {
          throw new Error(data && data.error ? data.error : "操作失败（" + response.status + "）");
        }
        return data;
      });
    });
  }

  var toastTimer = null;
  function toast(message, isError) {
    el.toast.textContent = message;
    el.toast.classList.toggle("error", !!isError);
    el.toast.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { el.toast.hidden = true; }, 2600);
  }

  function fail(error) { toast(error && error.message ? error.message : "操作失败", true); }

  // ------------------------------------------------------------- 渲染

  function fillCategorySelects() {
    [el["category-select"], el["edit-category"]].forEach(function (select) {
      if (!select) { return; }
      var previous = select.value;
      select.textContent = "";
      state.categories.forEach(function (category) {
        var option = document.createElement("option");
        option.value = String(category.id);
        option.textContent = category.name + (category.is_default ? "（默认）" : "");
        select.appendChild(option);
      });
      if (previous && select.querySelector('option[value="' + previous + '"]')) {
        select.value = previous;
      } else if (state.defaultCategoryId) {
        select.value = String(state.defaultCategoryId);
      }
    });
  }

  function renderCategories() {
    el["category-list"].textContent = "";
    var all = document.createElement("li");
    all.className = state.currentCategory === null ? "active" : "";
    var allName = document.createElement("span");
    allName.className = "cat-name";
    allName.textContent = "全部记录";
    var allCount = document.createElement("span");
    allCount.className = "cat-count";
    allCount.textContent = String(state.stats.total);
    all.appendChild(allName);
    all.appendChild(allCount);
    all.addEventListener("click", function () { selectCategory(null); });
    el["category-list"].appendChild(all);

    state.categories.forEach(function (category) {
      var item = document.createElement("li");
      item.className = state.currentCategory === category.id ? "active" : "";

      var name = document.createElement("span");
      name.className = "cat-name";
      name.textContent = category.name;
      name.title = category.name;

      var count = document.createElement("span");
      count.className = "cat-count";
      count.textContent = String(category.count);

      item.appendChild(name);
      item.appendChild(count);

      if (!category.is_default) {
        var actions = document.createElement("span");
        actions.className = "cat-actions";
        var renameBtn = document.createElement("button");
        renameBtn.type = "button";
        renameBtn.className = "link-btn";
        renameBtn.textContent = "改名";
        renameBtn.addEventListener("click", function (event) {
          event.stopPropagation();
          renameCategory(category);
        });
        var deleteBtn = document.createElement("button");
        deleteBtn.type = "button";
        deleteBtn.className = "link-btn danger";
        deleteBtn.textContent = "删除";
        deleteBtn.addEventListener("click", function (event) {
          event.stopPropagation();
          deleteCategory(category);
        });
        actions.appendChild(renameBtn);
        actions.appendChild(deleteBtn);
        item.appendChild(actions);
      }

      item.addEventListener("click", function () { selectCategory(category.id); });
      el["category-list"].appendChild(item);
    });

    el["total-count"].textContent = state.stats.total + " 条记录";
  }

  function currentTitle() {
    if (state.query) {
      return "搜索：" + state.query;
    }
    if (state.currentCategory === null) {
      return "全部记录";
    }
    var found = state.categories.filter(function (c) { return c.id === state.currentCategory; })[0];
    return found ? found.name : "记录";
  }

  function ordered() {
    var items = state.bookmarks.slice();
    items.sort(function (a, b) {
      var diff = String(a.created_at).localeCompare(String(b.created_at));
      if (diff === 0) { diff = a.id - b.id; }
      return state.newestFirst ? -diff : diff;
    });
    return items;
  }

  function formatDate(iso) {
    if (!iso) { return ""; }
    return String(iso).slice(0, 10);
  }

  function renderBookmarks() {
    el["list-title"].textContent = currentTitle();
    el["bookmark-list"].textContent = "";
    var items = ordered();
    el["list-hint"].textContent = state.query
      ? "找到 " + items.length + " 条与关键字相关的记录"
      : "共 " + items.length + " 条记录";

    if (items.length === 0) {
      el["empty-state"].hidden = false;
      el["empty-state"].textContent = state.query
        ? "没有找到匹配的记录，换个关键字试试。"
        : "这里还没有记录。把浏览时看到的链接保存进来吧。";
      return;
    }
    el["empty-state"].hidden = true;

    items.forEach(function (item) {
      var li = document.createElement("li");
      li.className = "bookmark";

      var top = document.createElement("div");
      top.className = "row-top";
      var link = document.createElement("a");
      link.className = "title";
      link.href = "/open/" + item.id;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.textContent = item.title || item.url;
      link.addEventListener("click", function () {
        setTimeout(function () { refreshStats(); }, 800);
      });
      top.appendChild(link);
      li.appendChild(top);

      var url = document.createElement("span");
      url.className = "url";
      url.textContent = item.url;
      li.appendChild(url);

      if (item.note) {
        var note = document.createElement("p");
        note.className = "note";
        note.textContent = item.note;
        li.appendChild(note);
      }

      var meta = document.createElement("div");
      meta.className = "meta";
      var tag = document.createElement("span");
      tag.className = "tag";
      tag.textContent = item.category_name;
      meta.appendChild(tag);

      var created = document.createElement("span");
      created.className = "muted";
      created.textContent = "保存于 " + formatDate(item.created_at);
      meta.appendChild(created);

      if (item.open_count > 0) {
        var opened = document.createElement("span");
        opened.className = "muted";
        opened.textContent = "已打开 " + item.open_count + " 次";
        meta.appendChild(opened);
      }

      var actions = document.createElement("span");
      actions.className = "actions";
      var editBtn = document.createElement("button");
      editBtn.type = "button";
      editBtn.className = "link-btn";
      editBtn.textContent = "编辑 / 移动";
      editBtn.addEventListener("click", function () { openEdit(item); });
      var deleteBtn = document.createElement("button");
      deleteBtn.type = "button";
      deleteBtn.className = "link-btn danger";
      deleteBtn.textContent = "删除";
      deleteBtn.addEventListener("click", function () { removeBookmark(item); });
      actions.appendChild(editBtn);
      actions.appendChild(deleteBtn);
      meta.appendChild(actions);
      li.appendChild(meta);

      el["bookmark-list"].appendChild(li);
    });
  }

  function renderStats() {
    el["stats-line"].textContent =
      "共收藏 " + state.stats.total + " 条，已打开过 " + state.stats.opened + " 条";
  }

  // ------------------------------------------------------------- 数据操作

  function loadState() {
    return api("GET", "/api/state").then(function (data) {
      state.categories = data.categories || [];
      state.defaultCategoryId = data.default_category_id;
      state.stats = data.stats || { total: 0, opened: 0 };
      if (state.currentCategory !== null &&
          !state.categories.some(function (c) { return c.id === state.currentCategory; })) {
        state.currentCategory = null;
      }
      fillCategorySelects();
      renderCategories();
      renderStats();
    });
  }

  function loadBookmarks() {
    var params = [];
    if (state.currentCategory !== null) { params.push("category_id=" + state.currentCategory); }
    if (state.query) { params.push("q=" + encodeURIComponent(state.query)); }
    var suffix = params.length ? "?" + params.join("&") : "";
    return api("GET", "/api/bookmarks" + suffix).then(function (data) {
      state.bookmarks = data.bookmarks || [];
      renderBookmarks();
    });
  }

  function refreshStats() {
    return api("GET", "/api/state").then(function (data) {
      state.stats = data.stats || state.stats;
      state.categories = data.categories || state.categories;
      renderStats();
      renderCategories();
    }).catch(function () { /* 统计刷新失败不影响主流程 */ });
  }

  function refreshAll() {
    return loadState().then(loadBookmarks).then(refreshStats).catch(fail);
  }

  function selectCategory(id) {
    state.currentCategory = id;
    renderCategories();
    loadBookmarks().catch(fail);
  }

  // ------------------------------------------------------------- 交互

  function submitAdd(event) {
    event.preventDefault();
    var payload = {
      url: el["url-input"].value,
      title: el["title-input"].value,
      note: el["note-input"].value,
      category_id: Number(el["category-select"].value) || null
    };
    api("POST", "/api/bookmarks", payload).then(function () {
      el["url-input"].value = "";
      el["title-input"].value = "";
      el["note-input"].value = "";
      toast("已保存到「" + (state.categories.filter(function (c) {
        return c.id === payload.category_id;
      })[0] || { name: "收藏夹" }).name + "」");
      return refreshAll();
    }).catch(fail);
  }

  function submitCategory(event) {
    event.preventDefault();
    var name = el["category-name"].value.trim();
    if (!name) { return; }
    api("POST", "/api/categories", { name: name }).then(function () {
      el["category-name"].value = "";
      toast("已新建归类");
      return refreshAll();
    }).catch(fail);
  }

  function renameCategory(category) {
    var next = window.prompt("修改归类名称", category.name);
    if (next === null) { return; }
    api("PUT", "/api/categories/" + category.id, { name: next }).then(function () {
      toast("归类已改名");
      return refreshAll();
    }).catch(fail);
  }

  function deleteCategory(category) {
    var message = category.count > 0
      ? "删除归类「" + category.name + "」？其中 " + category.count + " 条记录会移动到默认归类。"
      : "删除归类「" + category.name + "」？";
    if (!window.confirm(message)) { return; }
    api("DELETE", "/api/categories/" + category.id).then(function (result) {
      toast(result.moved > 0 ? "已删除归类，" + result.moved + " 条记录已移动" : "已删除归类");
      return refreshAll();
    }).catch(fail);
  }

  function removeBookmark(item) {
    if (!window.confirm("删除记录「" + (item.title || item.url) + "」？此操作不可撤销。")) { return; }
    api("DELETE", "/api/bookmarks/" + item.id).then(function () {
      toast("已删除记录");
      return refreshAll();
    }).catch(fail);
  }

  function openEdit(item) {
    el["edit-id"].value = String(item.id);
    el["edit-url"].value = item.url;
    el["edit-title"].value = item.title || "";
    el["edit-note"].value = item.note || "";
    el["edit-hint"].textContent = "保存于 " + formatDate(item.created_at) +
      (item.open_count ? "，已打开 " + item.open_count + " 次" : "");
    fillCategorySelects();
    el["edit-category"].value = String(item.category_id);
    if (typeof el["edit-dialog"].showModal === "function") {
      el["edit-dialog"].showModal();
    } else {
      el["edit-dialog"].setAttribute("open", "");
    }
  }

  function closeEdit() {
    if (typeof el["edit-dialog"].close === "function") {
      el["edit-dialog"].close();
    } else {
      el["edit-dialog"].removeAttribute("open");
    }
  }

  function submitEdit(event) {
    event.preventDefault();
    var id = el["edit-id"].value;
    var payload = {
      url: el["edit-url"].value,
      title: el["edit-title"].value,
      note: el["edit-note"].value,
      category_id: Number(el["edit-category"].value) || null
    };
    api("PUT", "/api/bookmarks/" + id, payload).then(function () {
      closeEdit();
      toast("修改已保存");
      return refreshAll();
    }).catch(fail);
  }

  var searchTimer = null;
  function onSearchInput() {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(function () {
      state.query = el["search-input"].value.trim();
      loadBookmarks().catch(fail);
    }, 220);
  }

  function clearSearch() {
    el["search-input"].value = "";
    state.query = "";
    loadBookmarks().catch(fail);
  }

  function init() {
    cache();
    state.newestFirst = el["sort-toggle"].checked;
    el["add-form"].addEventListener("submit", submitAdd);
    el["category-form"].addEventListener("submit", submitCategory);
    el["edit-form"].addEventListener("submit", submitEdit);
    el["edit-cancel"].addEventListener("click", closeEdit);
    el["search-input"].addEventListener("input", onSearchInput);
    el["search-clear"].addEventListener("click", clearSearch);
    el["sort-toggle"].addEventListener("change", function () {
      state.newestFirst = el["sort-toggle"].checked;
      renderBookmarks();
    });
    refreshAll();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
