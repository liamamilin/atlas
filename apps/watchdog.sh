#!/bin/zsh
# 看门狗：系统无输入 ≥30min 或浏览器无连接 ≥30min → 关闭全部服务并通知
set -u
WS="/Users/milin/2026/软件开发/application-atlas"
VITE_PORT=5188
LIMIT_SEC=1800
ZERO=0

echo "$(date '+%H:%M:%S') watchdog: watching (limit ${LIMIT_SEC}s)" >> "$WS/apps/launcher.log"
while true; do
  sleep 60
  lsof -ti tcp:$VITE_PORT -sTCP:LISTEN >/dev/null 2>&1 || { echo "$(date '+%H:%M:%S') watchdog: vite gone, exit" >> "$WS/apps/launcher.log"; exit 0; }
  pgrep -f "drafts_api.py" >/dev/null 2>&1 || { echo "$(date '+%H:%M:%S') watchdog: api gone, exit" >> "$WS/apps/launcher.log"; exit 0; }

  idle=$(ioreg -c IOHIDSystem 2>/dev/null | awk '/HIDIdleTime/{print int($NF/1000000000); exit}')
  [ -z "$idle" ] && idle=0
  conns=$(lsof -ti tcp:$VITE_PORT -sTCP:ESTABLISHED 2>/dev/null | grep -v "^$" | wc -l | tr -d ' ')

  if (( idle >= LIMIT_SEC )) || (( conns == 0 )); then
    ZERO=$((ZERO+1))
  else
    ZERO=0
  fi
  echo "$(date '+%H:%M:%S') watchdog: idle=${idle}s conns=$conns zero-streak=${ZERO}min" >> "$WS/apps/launcher.log"

  if (( ZERO >= LIMIT_SEC / 60 )); then
    pkill -f "drafts_api.py" 2>/dev/null
    pkill -f "vite --port $VITE_PORT" 2>/dev/null
    pkill -f "vite.*--port $VITE_PORT" 2>/dev/null
    echo "$(date '+%H:%M:%S') watchdog: SHUT DOWN (30min no activity)" >> "$WS/apps/launcher.log"
    osascript -e 'display notification "30 分钟无活动，atlas 服务已自动关闭" with title "Atlas 启动器"'
    exit 0
  fi
done
