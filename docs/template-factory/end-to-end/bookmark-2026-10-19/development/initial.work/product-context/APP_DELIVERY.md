# Application delivery protocol / 应用交付协议

This file defines source submission for the independent offline runtime runner. It does not execute code or make an old blueprint runtime-capable. The factory can run frozen acceptance only when the immutable source contains `blueprint/acceptance/runner.json` with a valid `atlas.acceptance-runner.v1` binding for the frozen cases. Do not invent runner commands or edit frozen tests.

本协议只定义离线运行验收的应用源码提交格式。只有冻结源包含有效的 `blueprint/acceptance/runner.json`（`atlas.acceptance-runner.v1`）时，工厂才支持运行；不得猜测命令或修改冻结验收程序。旧模板不会因此自动获得运行支持。

## ZIP layout and inventory

Submit a source-only ZIP no larger than 1 MiB compressed or 8 MiB expanded. Place `delivery.json` at ZIP root, beside the application files; do not wrap everything in another directory. Do not include real credentials, `.env` files, private keys, dependency caches, `node_modules` or virtual environments. The runner has no network access. Dependencies must be available in its managed offline image or included as allowed source assets; a network install is unavailable.

`schema` must equal `atlas.application-delivery.v1`. `root` is `.` or `app`. `files` must list every application source file exactly, excluding `delivery.json`; wildcards and omissions are rejected. A single unambiguous `app/` prefix may be normalized to match files placed at ZIP root or beneath `app/`; duplicates, collisions and repeated prefixes are rejected.

The following is a complete valid static-web example when the ZIP also contains the listed `index.html` file:

```json
{
  "schema": "atlas.application-delivery.v1",
  "root": ".",
  "files": ["index.html"],
  "runtime": {
    "profile": "static-web",
    "install": [],
    "build": [],
    "start": ["python3", "-m", "http.server", "8000"],
    "port": 8000,
    "readiness_path": "/"
  }
}
```

## Runtime profiles

Web profiles are `python-web`, `node-web` and `static-web`. Each requires a project-specific `start` argv and an integer `port` from 1024 to 65535; optional `readiness_path` defaults to `/`. `install` and `build` are optional lists of argv commands. Use only the profile's supplied executables: Python commands for `python-web` and `static-web`, Node/npm commands for `node-web`. `cli` requires a `smoke` argv instead of web startup fields and accepts Python CLI executables. These argv values are application delivery metadata, never acceptance commands; acceptance commands come only from the frozen runner binding.

CLI example shape (declare the exact files present in the ZIP):

```json
{
  "schema": "atlas.application-delivery.v1",
  "root": ".",
  "files": ["app.py"],
  "runtime": {"profile": "cli", "install": [], "build": [], "smoke": ["python3", "app.py"]}
}
```

## Evidence and completion report

Report the exact command used to start the app and the actual command/result for each test: passed, failed or not run. Preserve case IDs, captured output and assertion details. Exit code zero by itself does not establish user behavior; fix application defects rather than weakening frozen acceptance. Never describe an aborted, not-run or unverified case as passed.

报告实际启动命令及每项测试的实际命令和结果（通过、失败、未运行），保留用例编号、输出和断言细节。单独退出码为零不能证明用户行为通过；应修复应用，不得弱化冻结验收。中止、未运行或未核实用例不得写成通过。
