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

[ -f "$LOG" ] && : > "$LOG"
echo "$(date '+%H:%M:%S') launcher: start" >> "$LOG"

# 用子 shell 二次 fork 并 nohup，让服务脱离 .app 的进程组/LaunchServices 会话。
# 否则服务进程会继承 app 的 bundle id，后续再次点图标时 macOS 会返回 -600 拒绝启动。
if ! running_api; then
  ( cd "$PACK" && nohup python3 drafts_api.py >> "$LOG" 2>&1 & )
  echo "$(date '+%H:%M:%S') started drafts_api" >> "$LOG"
fi
if ! running_vite; then
  ( cd "$WEB" && nohup npm run dev >> "$LOG" 2>&1 & )
  echo "$(date '+%H:%M:%S') started vite" >> "$LOG"
fi

# 等服务就绪后打开浏览器
for i in {1..20}; do
  curl -s -o /dev/null "http://localhost:$VITE_PORT" && break
  sleep 0.5
done
open "http://localhost:$VITE_PORT"

# 看门狗（幂等：先清旧的）
pkill -f "apps/watchdog.sh" 2>/dev/null
( nohup zsh "$WS/apps/watchdog.sh" >> "$LOG" 2>&1 & )
echo "$(date '+%H:%M:%S') watchdog started (idle limit ${IDLE_LIMIT_MIN}min)" >> "$LOG"
