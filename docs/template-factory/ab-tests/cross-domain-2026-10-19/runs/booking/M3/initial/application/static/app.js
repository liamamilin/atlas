/* 社区共享设施预约 —— 前端逻辑（原生 JS，无第三方依赖）。 */
"use strict";

const $ = (sel) => document.querySelector(sel);

const state = { user: null, resources: [] };

async function api(path, method = "GET", body) {
  const options = { method, headers: {} };
  if (body !== undefined) {
    options.headers["Content-Type"] = "application/json";
    options.body = JSON.stringify(body);
  }
  const res = await fetch(path, options);
  let data = null;
  try { data = await res.json(); } catch (e) { data = null; }
  return { status: res.status, ok: res.ok, data };
}

function message(text, kind) {
  const el = $("#message");
  el.textContent = text || "";
  el.className = "message" + (kind ? " " + kind : "");
}

function errorText(result, fallback) {
  if (result && result.data && result.data.error) return result.data.error;
  return fallback;
}

function roleLabel(role) {
  if (role === "admin") return "设施管理员";
  if (role === "resident") return "居民";
  return role || "";
}

function resourceName(id) {
  const found = state.resources.find((r) => r.id === id);
  return found ? found.name : ("#" + id);
}

function statusLabel(status) {
  if (status === "active") return "生效中";
  if (status === "cancelled") return "已取消";
  return status;
}

/* ------------------------------------------------------------ 视图切换 */

function showLogin() {
  state.user = null;
  $("#login-view").hidden = false;
  $("#app-view").hidden = true;
  $("#user-bar").textContent = "";
}

async function enterApp() {
  $("#login-view").hidden = true;
  $("#app-view").hidden = false;
  $("#user-bar").textContent =
    state.user.username + "（" + roleLabel(state.user.role) + "）";
  $("#admin-panel").hidden = state.user.role !== "admin";
  await loadResources();
  await loadBookings();
}

/* ------------------------------------------------------------ 数据加载 */

async function loadResources() {
  const result = await api("/api/resources");
  state.resources = result.ok && result.data ? result.data.resources || [] : [];
  const select = $('[data-testid="booking-resource"]');
  const previous = select.value;
  select.textContent = "";
  if (state.resources.length === 0) {
    const opt = document.createElement("option");
    opt.value = "";
    opt.textContent = "暂无设施";
    select.appendChild(opt);
  } else {
    for (const resource of state.resources) {
      const opt = document.createElement("option");
      opt.value = String(resource.id);
      opt.textContent = resource.name;
      select.appendChild(opt);
    }
    if (previous && state.resources.some((r) => String(r.id) === previous)) {
      select.value = previous;
    }
  }
  await loadAvailability();
}

async function loadAvailability() {
  const box = $("#availability");
  box.textContent = "";
  const resourceId = $('[data-testid="booking-resource"]').value;
  if (!resourceId) return;
  const result = await api("/api/availability?resource_id=" + encodeURIComponent(resourceId));
  if (!result.ok || !result.data) {
    box.textContent = "无法获取占用时段：" + errorText(result, "未知错误");
    return;
  }
  const slots = result.data.slots || [];
  if (slots.length === 0) {
    box.textContent = "当前没有已占用时段，可自由预约。";
    return;
  }
  const title = document.createElement("div");
  title.textContent = "已被占用的时段：";
  box.appendChild(title);
  for (const slot of slots) {
    const chip = document.createElement("span");
    chip.className = "slot";
    chip.textContent = slot.start + " → " + slot.end;
    box.appendChild(chip);
  }
}

async function loadBookings() {
  const list = $("#booking-list");
  list.textContent = "";
  const result = await api("/api/bookings");
  if (!result.ok || !result.data) {
    const p = document.createElement("p");
    p.className = "empty";
    p.textContent = "无法获取预约记录：" + errorText(result, "未知错误");
    list.appendChild(p);
    return;
  }
  const bookings = result.data.bookings || [];
  if (bookings.length === 0) {
    const p = document.createElement("p");
    p.className = "empty";
    p.textContent = "暂无预约记录。";
    list.appendChild(p);
    return;
  }
  for (const booking of bookings) {
    list.appendChild(renderBooking(booking));
  }
}

function renderBooking(booking) {
  const row = document.createElement("div");
  row.className = "booking";

  const info = document.createElement("div");
  const line1 = document.createElement("div");
  line1.textContent = "设施 #" + booking.resource_id + "（" + resourceName(booking.resource_id) + "）";
  const line2 = document.createElement("div");
  line2.className = "meta";
  line2.textContent = booking.start + " → " + booking.end;
  info.appendChild(line1);
  info.appendChild(line2);
  if (booking.note) {
    const note = document.createElement("div");
    note.className = "meta";
    note.textContent = "备注：" + booking.note;
    info.appendChild(note);
  }
  if (state.user && state.user.role === "admin") {
    const owner = document.createElement("div");
    owner.className = "meta";
    owner.textContent = "预约人 ID：" + booking.owner_id;
    info.appendChild(owner);
  }

  const right = document.createElement("div");
  const status = document.createElement("span");
  status.className = booking.status === "active" ? "status-active" : "status-cancelled";
  status.textContent = statusLabel(booking.status);
  right.appendChild(status);

  if (booking.status === "active") {
    const cancel = document.createElement("button");
    cancel.type = "button";
    cancel.className = "link";
    cancel.textContent = "取消";
    cancel.addEventListener("click", () => cancelBooking(booking.id));
    right.appendChild(document.createTextNode(" "));
    right.appendChild(cancel);
  }

  row.appendChild(info);
  row.appendChild(right);
  return row;
}

/* ------------------------------------------------------------ 操作 */

async function doLogin(event) {
  event.preventDefault();
  const username = $('[data-testid="login-username"]').value.trim();
  const password = $('[data-testid="login-password"]').value;
  const result = await api("/api/login", "POST", { username, password });
  if (!result.ok || !result.data) {
    message(errorText(result, "登录失败"), "error");
    return;
  }
  state.user = result.data.user;
  message("登录成功。", "ok");
  await enterApp();
}

async function doCreateResource(event) {
  event.preventDefault();
  const input = $('[data-testid="resource-name"]');
  const name = input.value.trim();
  if (!name) {
    message("请输入设施名称。", "error");
    return;
  }
  const result = await api("/api/resources", "POST", { name });
  if (!result.ok || !result.data) {
    message(errorText(result, "创建设施失败"), "error");
    return;
  }
  input.value = "";
  message("已创建设施：" + name, "ok");
  await loadResources();
}

async function doCreateBooking(event) {
  event.preventDefault();
  const resourceId = $('[data-testid="booking-resource"]').value;
  const start = $('[data-testid="booking-start"]').value.trim();
  const end = $('[data-testid="booking-end"]').value.trim();
  const note = $('[data-testid="booking-note"]').value;
  if (!resourceId) {
    message("请先选择设施（需管理员先创建）。", "error");
    return;
  }
  const result = await api("/api/bookings", "POST", {
    resource_id: Number(resourceId),
    start,
    end,
    note,
  });
  if (!result.ok || !result.data) {
    message(errorText(result, "预约失败"), "error");
    return;
  }
  message("预约成功，编号 #" + result.data.id, "ok");
  $('[data-testid="booking-start"]').value = "";
  $('[data-testid="booking-end"]').value = "";
  $('[data-testid="booking-note"]').value = "";
  await loadAvailability();
  await loadBookings();
}

async function cancelBooking(id) {
  const result = await api("/api/bookings/" + id + "/cancel", "POST");
  if (!result.ok || !result.data) {
    message(errorText(result, "取消失败"), "error");
    return;
  }
  message("预约 #" + id + " 已取消。", "ok");
  await loadAvailability();
  await loadBookings();
}

async function doLogout() {
  await api("/api/logout", "POST");
  message("已退出登录。", "ok");
  showLogin();
}

/* ------------------------------------------------------------ 初始化 */

function bindEvents() {
  $("#login-form").addEventListener("submit", doLogin);
  $("#resource-form").addEventListener("submit", doCreateResource);
  $("#booking-form").addEventListener("submit", doCreateBooking);
  $("#logout-btn").addEventListener("click", doLogout);
  $('[data-testid="booking-resource"]').addEventListener("change", loadAvailability);
}

async function init() {
  bindEvents();
  const result = await api("/api/me");
  if (result.ok && result.data && result.data.user) {
    state.user = result.data.user;
    await enterApp();
  } else {
    showLogin();
  }
}

document.addEventListener("DOMContentLoaded", init);
