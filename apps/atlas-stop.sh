#!/bin/zsh
# Atlas 停止：立即关闭全部服务与看门狗
WS="/Users/milin/2026/软件开发/application-atlas"
pkill -f "apps/watchdog.sh" 2>/dev/null
pkill -f "drafts_api.py" 2>/dev/null
pkill -f "vite --port 5188" 2>/dev/null
pkill -f "vite.*--port 5188" 2>/dev/null
echo "$(date '+%H:%M:%S') manual stop" >> "$WS/apps/launcher.log"
osascript -e 'display notification "atlas 服务已停止" with title "Atlas 启动器"'
