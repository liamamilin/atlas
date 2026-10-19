/* 社区共享设施预约 —— 前端交互（原生 JS，无第三方依赖）。
   所有状态均来自真实 JSON API，与 GET / 共享同一份服务端状态。 */
(function () {
  "use strict";

  var API = window.ATLAS_ENDPOINTS;
  var state = { user: null, resources: [] };

  function $(id) { return document.getElementById(id); }

  function show(el, visible) { if (el) { el.hidden = !visible; } }

  function message(text, kind) {
    var box = $("message");
    if (!box) { return; }
    box.textContent = text || "";
    box.className = "message" + (kind ? " " + kind : "");
  }

  function request(path, options) {
    options = options || {};
    var init = { method: options.method || "GET", credentials: "same-origin", headers: {} };
    if (options.body !== undefined) {
      init.headers["Content-Type"] = "application/json";
      init.body = JSON.stringify(options.body);
    }
    return fetch(path, init).then(function (resp) {
      return resp.json().catch(function () { return {}; }).then(function (data) {
        if (!resp.ok) {
          var text = data && (data.error || data.reason || data.message);
          var err = new Error(text || ("请求失败（" + resp.status + "）"));
          err.status = resp.status;
          throw err;
        }
        return data;
      });
    });
  }

  function applySession() {
    var loggedIn = !!state.user;
    show($("login-panel"), !loggedIn);
    show($("session-box"), loggedIn);
    show($("booking-panel"), loggedIn);
    show($("availability-panel"), loggedIn);
    show($("bookings-panel"), loggedIn);
    show($("admin-panel"), loggedIn && state.user.role === "admin");
    if (loggedIn) {
      $("session-user").textContent = state.user.username + "（" +
        (state.user.role === "admin" ? "设施管理员" : "居民") + "）";
      $("bookings-title").textContent = state.user.role === "admin"
        ? "全部预约记录（管理员）" : "我的预约记录";
    }
  }

  function refresh() {
    return request(API.me).then(function (data) {
      state.user = data.user;
      applySession();
      return loadResources();
    }).catch(function () {
      state.user = null;
      state.resources = [];
      applySession();
    });
  }

  function loadResources() {
    return request(API.resources).then(function (data) {
      state.resources = data.resources || [];
      var select = $("booking-resource");
      select.innerHTML = "";
      state.resources.forEach(function (r) {
        var option = document.createElement("option");
        option.value = String(r.id);
        option.textContent = r.name;
        select.appendChild(option);
      });
      return loadBookings().then(loadAvailability);
    });
  }

  function loadAvailability() {
    var select = $("booking-resource");
    var list = $("availability-list");
    list.innerHTML = "";
    if (!select.value) { return Promise.resolve(); }
    return request(API.availability + "?resource_id=" + encodeURIComponent(select.value))
      .then(function (data) {
        var slots = data.slots || [];
        if (!slots.length) {
          var li = document.createElement("li");
          li.className = "empty";
          li.textContent = "该设施当前没有占用时段。";
          list.appendChild(li);
          return;
        }
        slots.forEach(function (slot) {
          var item = document.createElement("li");
          item.textContent = slot.start + " → " + slot.end;
          list.appendChild(item);
        });
      })
      .catch(function (err) { message(err.message, "error"); });
  }

  function resourceName(id) {
    for (var i = 0; i < state.resources.length; i++) {
      if (String(state.resources[i].id) === String(id)) { return state.resources[i].name; }
    }
    return String(id);
  }

  function renderBookingRow(booking) {
    var tr = document.createElement("tr");
    [booking.id, resourceName(booking.resource_id), booking.start, booking.end,
     booking.status === "active" ? "有效" : "已取消", booking.note || ""]
      .forEach(function (value) {
        var td = document.createElement("td");
        td.textContent = String(value);
        tr.appendChild(td);
      });
    var actions = document.createElement("td");
    if (booking.status === "active") {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "btn small";
      btn.textContent = "取消";
      btn.addEventListener("click", function () { cancelBooking(booking.id); });
      actions.appendChild(btn);
    } else {
      actions.textContent = "—";
    }
    tr.appendChild(actions);
    return tr;
  }

  function loadBookings() {
    var body = $("bookings-body");
    body.innerHTML = "";
    return request(API.bookings).then(function (data) {
      var bookings = data.bookings || [];
      if (!bookings.length) {
        var tr = document.createElement("tr");
        var td = document.createElement("td");
        td.colSpan = 7;
        td.textContent = "暂无预约记录。";
        tr.appendChild(td);
        body.appendChild(tr);
        return;
      }
      bookings.forEach(function (booking) { body.appendChild(renderBookingRow(booking)); });
    });
  }

  function cancelBooking(id) {
    request(API.bookings + "/" + id + "/cancel", { method: "POST" })
      .then(function () {
        message("预约 #" + id + " 已取消。", "ok");
        return loadResources();
      })
      .catch(function (err) { message(err.message, "error"); });
  }

  function login() {
    message("");
    request(API.login, {
      method: "POST",
      body: { username: $("login-username").value.trim(), password: $("login-password").value }
    }).then(function () {
      $("login-password").value = "";
      message("登录成功。", "ok");
      return refresh();
    }).catch(function (err) { message(err.message, "error"); });
  }

  function logout() {
    request(API.logout, { method: "POST" }).then(function () {
      message("已登出。", "ok");
      return refresh();
    }).catch(function (err) { message(err.message, "error"); });
  }

  function createResource() {
    var name = $("resource-name").value.trim();
    if (!name) { message("请输入设施名称。", "error"); return; }
    request(API.resources, { method: "POST", body: { name: name } })
      .then(function () {
        $("resource-name").value = "";
        message("设施已创建。", "ok");
        return loadResources();
      })
      .catch(function (err) { message(err.message, "error"); });
  }

  function createBooking() {
    var select = $("booking-resource");
    if (!select.value) { message("请先选择设施。", "error"); return; }
    request(API.bookings, {
      method: "POST",
      body: {
        resource_id: Number(select.value),
        start: $("booking-start").value.trim(),
        end: $("booking-end").value.trim(),
        note: $("booking-note").value.trim()
      }
    }).then(function () {
      $("booking-note").value = "";
      message("预约提交成功。", "ok");
      return loadResources();
    }).catch(function (err) { message(err.message, "error"); });
  }

  function bind(id, handler) {
    var el = $(id);
    if (el) { el.addEventListener("click", handler); }
  }

  document.addEventListener("DOMContentLoaded", function () {
    bind("login-submit", login);
    bind("logout-btn", logout);
    bind("resource-save", createResource);
    bind("booking-save", createBooking);
    var select = $("booking-resource");
    if (select) { select.addEventListener("change", loadAvailability); }
    refresh();
  });
})();
