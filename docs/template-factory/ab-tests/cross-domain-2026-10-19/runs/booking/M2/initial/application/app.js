/* 社区共享设施预约 —— 前端逻辑（原生 JS，无第三方依赖）。
   全部通过真实 JSON API 读写，与服务端状态一致；按登录与角色显示控件。 */
(function () {
  'use strict';

  var cfg = window.APP_CONFIG || {};
  var state = { user: null, resources: [], bookings: [] };

  function el(id) { return document.getElementById(id); }

  function feedback(message, kind) {
    var node = el('feedback');
    node.textContent = message || '';
    node.className = 'feedback' + (kind ? ' ' + kind : '');
  }

  function api(method, path, body) {
    var options = { method: method, headers: {}, credentials: 'same-origin' };
    if (body !== undefined && body !== null) {
      options.headers['Content-Type'] = 'application/json';
      options.body = JSON.stringify(body);
    }
    return fetch(path, options).then(function (response) {
      return response.json().catch(function () { return null; }).then(function (data) {
        if (!response.ok) {
          var message = (data && (data.error || data.message)) ||
            ('请求失败（HTTP ' + response.status + '）');
          var error = new Error(message);
          error.status = response.status;
          throw error;
        }
        return data;
      });
    });
  }

  // -- 渲染 ---------------------------------------------------------------
  function render() {
    var loggedIn = !!state.user;
    var isAdmin = loggedIn && state.user.role === 'admin';
    var isResident = loggedIn && state.user.role === 'resident';

    el('login-panel').hidden = loggedIn;
    el('logout').hidden = !loggedIn;
    el('admin-panel').hidden = !isAdmin;
    el('resident-panel').hidden = !isResident;
    el('content-panel').hidden = !loggedIn;

    el('user-label').textContent = loggedIn
      ? state.user.username + '（' + (isAdmin ? '设施管理员' : '居民') + '）'
      : '未登录';

    renderResourceList();
    fillResourceSelect();
    renderBookings();
  }

  function renderResourceList() {
    var list = el('resource-list');
    list.innerHTML = '';
    if (!state.resources.length) {
      list.appendChild(item('（暂无设施，管理员可在上方创建）', null));
      return;
    }
    state.resources.forEach(function (resource) {
      var button = document.createElement('button');
      button.type = 'button';
      button.className = 'ghost';
      button.textContent = '查看占用时段';
      button.addEventListener('click', function () { showAvailability(resource.id); });
      var row = document.createElement('li');
      row.appendChild(span(resource.name));
      row.appendChild(button);
      list.appendChild(row);
    });
  }

  function item(text, action) {
    var row = document.createElement('li');
    row.appendChild(span(text));
    if (action) { row.appendChild(action); }
    return row;
  }

  function span(text) {
    var node = document.createElement('span');
    node.textContent = text;
    return node;
  }

  function fillResourceSelect() {
    var select = el('booking-resource');
    var previous = select.value;
    select.innerHTML = '';
    state.resources.forEach(function (resource) {
      var option = document.createElement('option');
      option.value = String(resource.id);   // option value 必须等于 resource_id
      option.textContent = resource.name;
      select.appendChild(option);
    });
    if (previous) { select.value = previous; }
  }

  function resourceName(id) {
    for (var i = 0; i < state.resources.length; i += 1) {
      if (state.resources[i].id === id) { return state.resources[i].name; }
    }
    return '#' + id;
  }

  function renderBookings() {
    var body = el('booking-body');
    body.innerHTML = '';
    var table = el('booking-table');
    var empty = el('booking-empty');
    var admin = state.user && state.user.role === 'admin';

    if (!state.bookings.length) {
      table.hidden = true;
      empty.hidden = false;
      return;
    }
    table.hidden = false;
    empty.hidden = true;

    state.bookings.forEach(function (booking) {
      var row = document.createElement('tr');

      row.appendChild(cell('#' + booking.id));
      row.appendChild(cell(resourceName(booking.resource_id)));
      row.appendChild(cell(booking.start));
      row.appendChild(cell(booking.end));
      row.appendChild(cell(booking.note || ''));

      var status = document.createElement('td');
      status.textContent = booking.status === 'active' ? '有效' : '已取消';
      status.className = booking.status === 'active' ? 'status-active' : 'status-cancelled';
      row.appendChild(status);

      var actions = document.createElement('td');
      if (booking.status === 'active' && (admin || booking.owner_id === state.user.id)) {
        var cancel = document.createElement('button');
        cancel.type = 'button';
        cancel.className = 'danger';
        cancel.textContent = '取消';
        cancel.addEventListener('click', function () { cancelBooking(booking.id); });
        actions.appendChild(cancel);
      } else {
        actions.textContent = '—';
      }
      row.appendChild(actions);

      body.appendChild(row);
    });
  }

  function cell(text) {
    var node = document.createElement('td');
    node.textContent = text;
    return node;
  }

  // -- 数据加载 -----------------------------------------------------------
  function refreshSession() {
    return api('GET', cfg.me).then(function (data) {
      state.user = data.user || null;
    }).catch(function (error) {
      state.user = null;
      if (error.status !== 401) { feedback(error.message, 'error'); }
    }).then(render);
  }

  function loadResources() {
    if (!state.user) { state.resources = []; return Promise.resolve(); }
    return api('GET', cfg.resources).then(function (data) {
      state.resources = data.resources || [];
    }).catch(function (error) { feedback(error.message, 'error'); });
  }

  function loadBookings() {
    if (!state.user) { state.bookings = []; return Promise.resolve(); }
    return api('GET', cfg.bookings).then(function (data) {
      state.bookings = data.bookings || [];
    }).catch(function (error) { feedback(error.message, 'error'); });
  }

  function loadAll() {
    return loadResources().then(loadBookings).then(render);
  }

  function showAvailability(resourceId) {
    api('GET', cfg.availability + '?resource_id=' + encodeURIComponent(resourceId))
      .then(function (data) {
        var slots = data.slots || [];
        var name = resourceName(resourceId);
        if (!slots.length) {
          el('availability').textContent = name + '：暂无占用时段，可预约。';
          return;
        }
        var lines = slots.map(function (slot) {
          return '• ' + slot.start + '  →  ' + slot.end;
        });
        el('availability').textContent = name + ' 已占用时段：\n' + lines.join('\n');
      })
      .catch(function (error) { feedback(error.message, 'error'); });
  }

  // -- 交互 ---------------------------------------------------------------
  function onLogin(event) {
    event.preventDefault();
    var username = el('login-username').value.trim();
    var password = el('login-password').value;
    if (!username || !password) { feedback('请输入用户名和密码。', 'error'); return; }
    api('POST', cfg.login, { username: username, password: password })
      .then(function (data) {
        state.user = data.user || null;
        el('login-password').value = '';
        feedback('登录成功。', 'ok');
        return loadAll();
      })
      .catch(function (error) { feedback(error.message, 'error'); });
  }

  function onLogout() {
    api('POST', cfg.logout).then(function () {
      state.user = null;
      state.resources = [];
      state.bookings = [];
      el('availability').textContent = '请选择设施查看占用时段。';
      feedback('已退出登录。', 'ok');
      render();
    }).catch(function (error) { feedback(error.message, 'error'); });
  }

  function onResourceCreate(event) {
    event.preventDefault();
    var name = el('resource-name').value.trim();
    if (!name) { feedback('请输入设施名称。', 'error'); return; }
    api('POST', cfg.resources, { name: name }).then(function () {
      el('resource-name').value = '';
      feedback('设施已创建。', 'ok');
      return loadResources().then(render);
    }).catch(function (error) { feedback(error.message, 'error'); });
  }

  function onBookingCreate(event) {
    event.preventDefault();
    var resourceId = el('booking-resource').value;
    var start = el('booking-start').value.trim();
    var end = el('booking-end').value.trim();
    var note = el('booking-note').value.trim();
    if (!resourceId) { feedback('请先选择设施。', 'error'); return; }
    if (!start || !end) { feedback('请填写开始与结束时间。', 'error'); return; }
    api('POST', cfg.bookings, {
      resource_id: Number(resourceId), start: start, end: end, note: note
    }).then(function () {
      el('booking-note').value = '';
      feedback('预约成功。', 'ok');
      return loadBookings().then(render);
    }).catch(function (error) { feedback(error.message, 'error'); });
  }

  function cancelBooking(id) {
    api('POST', cfg.bookings + '/' + id + '/cancel').then(function () {
      feedback('预约已取消。', 'ok');
      return loadBookings().then(render);
    }).catch(function (error) { feedback(error.message, 'error'); });
  }

  function bind() {
    el('login-form').addEventListener('submit', onLogin);
    el('logout').addEventListener('click', onLogout);
    el('resource-form').addEventListener('submit', onResourceCreate);
    el('booking-form').addEventListener('submit', onBookingCreate);
  }

  function start() {
    bind();
    refreshSession().then(loadAll);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
