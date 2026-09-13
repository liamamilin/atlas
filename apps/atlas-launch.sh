#!/bin/zsh
# Atlas 启动器主逻辑：起服务（幂等）+ 开浏览器 + 拉起看门狗
set -u
WS="/Users/milin/2026/软件开发/application-atlas"
PACK="$WS/application-atlas-production-pack"
WEB="$WS/atlas-web"
LOG="$WS/apps/launcher.log"
IDLE_LIMIT_MIN=30        # 无活动多少分钟后自动关闭
VITE_PORT=5188

running_vite()  { lsof -ti tcp:$VITE_PORT -sTCP:LISTEN >/dev/null 2>&1; }
running_api()   { pgrep -f "drafts_api.py" >/dev/null 2>&1; }

[ -f "$LOG" ] && : > "$LOG"
echo "$(date '+%H:%M:%S') launcher: start" >> "$LOG"

if ! running_api; then
  (cd "$PACK" && nohup python3 drafts_api.py >> "$LOG" 2>&1 &)
  echo "$(date '+%H:%M:%S') started drafts_api" >> "$LOG"
fi
if ! running_vite; then
  (cd "$WEB" && nohup npm run dev -- --port $VITE_PORT >> "$LOG" 2>&1 &)
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
nohup zsh "$WS/apps/watchdog.sh" >> "$LOG" 2>&1 &
echo "$(date '+%H:%M:%S') watchdog started (idle limit ${IDLE_LIMIT_MIN}min)" >> "$LOG"
