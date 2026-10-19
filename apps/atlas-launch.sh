#!/bin/zsh
# Atlas 启动器主逻辑：起服务（幂等）+ 开浏览器 + 拉起看门狗
set -u
WS="${0:A:h:h}"
PACK="$WS/application-atlas-production-pack"
WEB="$WS/atlas-web"
LOG="$WS/apps/launcher.log"
IDLE_LIMIT_MIN=30        # 无活动多少分钟后自动关闭
API_PORT=5199
VITE_PORT=5188

running_vite()  { lsof -ti tcp:$VITE_PORT -sTCP:LISTEN >/dev/null 2>&1; }
running_api()   { lsof -ti tcp:$API_PORT -sTCP:LISTEN >/dev/null 2>&1; }

# 进程启动时间（epoch 秒）。starttime 是 ps lstart，需转成 epoch。
api_is_stale() {
  running_api || return 1
  local pid started cutoff newest
  pid="$(lsof -ti tcp:$API_PORT -sTCP:LISTEN 2>/dev/null | head -1)"
  [[ -n "$pid" ]] || return 1
  started="$(ps -o lstart= -p "$pid" 2>/dev/null | xargs -0 -I{} date -j -f "%a %b %d %T %Y" "{}" "+%s" 2>/dev/null)"
  [[ -n "$started" ]] || return 1
  # BSD find 不接受 @epoch，必须传可读时间。
  cutoff="$(date -r "$started" "+%Y-%m-%d %H:%M:%S" 2>/dev/null)" || return 1
  newest="$(find "$PACK" -maxdepth 1 -name '*.py' -newermt "$cutoff" -print -quit 2>/dev/null)"
  [[ -n "$newest" ]]
}

[ -f "$LOG" ] && : > "$LOG"
echo "$(date '+%H:%M:%S') launcher: start" >> "$LOG"

# .app 从 Finder 启动时不会加载 ~/.zshrc，PATH 只有 launchd 默认值（/usr/bin:/bin:/usr/sbin:/sbin），
# 因此 python3 会落到系统自带的 3.9，npm 完全找不到。这里显式解析出 pyenv / nvm 里的运行时。
export PATH="/opt/homebrew/bin:/usr/local/bin:$HOME/.pyenv/shims:$PATH"

find_python() {
  local -a cands
  command -v python3 >/dev/null 2>&1 && cands+=("$(command -v python3)")
  cands+=("$HOME"/.pyenv/versions/*/bin/python3(N))
  cands+=(/opt/homebrew/bin/python3(N) /usr/local/bin/python3(N))
  local c
  for c in $cands; do
    [[ -x "$c" ]] || continue
    "$c" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' 2>/dev/null && { print -r -- "$c"; return 0 }
  done
  return 1
}

find_node_bin() {
  local -a cands
  command -v npm >/dev/null 2>&1 && cands+=("$(dirname "$(command -v npm)")")
  cands+=("$HOME"/.nvm/versions/node/*/bin(N) /opt/homebrew/bin(N) /usr/local/bin(N))
  local c
  for c in $cands; do
    [[ -x "$c/npm" ]] && { print -r -- "$c"; return 0 }
  done
  return 1
}

PYTHON_BIN="$(find_python)" || PYTHON_BIN=""
NODE_BIN="$(find_node_bin)" || NODE_BIN=""
[[ -n "$NODE_BIN" ]] && export PATH="$NODE_BIN:$PATH"
echo "$(date '+%H:%M:%S') launcher: python=${PYTHON_BIN:-MISSING} node=${NODE_BIN:-MISSING}" >> "$LOG"

for need in python node; do
  var="${need:u}_BIN"
  if [[ -z "${(P)var}" ]]; then
    echo "$(date '+%H:%M:%S') launcher: FATAL 未找到 $need（需要 Python 3.10+ / Node 22）" >> "$LOG"
    osascript -e "display notification \"找不到 $need，请检查 pyenv / nvm 安装\" with title \"Atlas 启动失败\"" 2>/dev/null
    exit 1
  fi
done

# 用子 shell 二次 fork 并 nohup，让服务脱离 .app 的进程组/LaunchServices 会话。
# 否则服务进程会继承 app 的 bundle id，后续再次点图标时 macOS 会返回 -600 拒绝启动。
if api_is_stale; then
  echo "$(date '+%H:%M:%S') api 源码比运行中的进程新，重启 drafts_api" >> "$LOG"
  pkill -f "drafts_api.py" 2>/dev/null
  for i in {1..20}; do running_api || break; sleep 0.25; done
fi
if ! running_api; then
  ( cd "$PACK" && nohup "$PYTHON_BIN" drafts_api.py >> "$LOG" 2>&1 & )
  echo "$(date '+%H:%M:%S') started drafts_api" >> "$LOG"
fi
if ! running_vite; then
  ( cd "$WEB" && nohup "$NODE_BIN/npm" run dev >> "$LOG" 2>&1 & )
  echo "$(date '+%H:%M:%S') started vite" >> "$LOG"
fi

# 等 API 就绪，再打开浏览器。只等 vite 会让新接口在页面加载时还没起来。
for i in {1..40}; do
  curl -s -o /dev/null "http://127.0.0.1:$API_PORT/api/health" && break
  sleep 0.5
done
# 等 vite 就绪后打开浏览器
for i in {1..20}; do
  curl -s -o /dev/null "http://localhost:$VITE_PORT" && break
  sleep 0.5
done
open "http://localhost:$VITE_PORT"

# 看门狗（幂等：先清旧的）
pkill -f "apps/watchdog.sh" 2>/dev/null
( nohup zsh "$WS/apps/watchdog.sh" >> "$LOG" 2>&1 & )
echo "$(date '+%H:%M:%S') watchdog started (idle limit ${IDLE_LIMIT_MIN}min)" >> "$LOG"
