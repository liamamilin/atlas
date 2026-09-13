#!/bin/bash
# Application Atlas batch production driver
#
# Usage:
#   ./batch.sh [N] [listfile]   process up to N pending leaves from listfile
#                               (N default 10; 0 = no limit; listfile default leaves.txt)
#   ./batch.sh 0                process ALL pending leaves (1805 total — long run!)
#
# Each leaf = one fresh `opencode run` session (zero context pollution).
# Progress tracked in STATUS.md; failures logged in batch.log.
# Safe to interrupt (Ctrl-C) and re-run: processed/failed leaves are skipped.
#
# Requires: .opencode/agents/atlas-writer.md + leaves.txt + STATUS.md

set -u
PACK_DIR="/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack"

# 防止 macOS 系统睡眠中断批量（熄屏不受影响，进程继续）
# 注意：笔记本需插电源；合盖仍会睡眠（caffeinate 无法阻止合盖睡眠）
if command -v caffeinate >/dev/null 2>&1 && [ "${ATLAS_CAFFEINATED:-0}" != "1" ]; then
  export ATLAS_CAFFEINATED=1
  exec caffeinate -is "$0" "$@"
fi

cd "$PACK_DIR" || exit 1
mkdir -p logs

LIMIT="${1:-10}"
LIST_FILE="${2:-leaves.txt}"
COUNT=0
DONE=0
FAILED=0

echo "[$(date '+%F %T')] batch.sh started (limit=${LIMIT:-unlimited}, list=${LIST_FILE})" | tee -a batch.log

while IFS='|' read -r slug name; do
  [ -z "$slug" ] && continue

  # skip if already processed (agent appends "- slug — date" under ## Processed)
  if grep -qF -- "- ${slug} " STATUS.md 2>/dev/null; then
    continue
  fi
  # skip if previously failed (grep batch.log)
  if grep -qF -- "FAIL ${slug} " batch.log 2>/dev/null; then
    continue
  fi

  # stop conditions
  COUNT=$((COUNT + 1))
  if [ "$LIMIT" -gt 0 ] && [ "$COUNT" -gt "$LIMIT" ]; then
    break
  fi

  echo "[$(date '+%F %T')] START ${slug} :: ${name}" | tee -a batch.log

  opencode run \
    --dir "$PACK_DIR" \
    --agent atlas-writer \
    --title "atlas: ${slug}" \
    --auto \
    "处理目录叶子：${name}（slug: ${slug}）。按 atlas-writer 工作指令完成全部流程并退出。" \
    < /dev/null \
    > "logs/${slug}.log" 2>&1
  RC=$?

  # success = agent updated STATUS.md
  if grep -qF -- "- ${slug} " STATUS.md 2>/dev/null; then
    echo "[$(date '+%F %T')] DONE  ${slug} (rc=${RC})" | tee -a batch.log
    DONE=$((DONE + 1))
  else
    echo "[$(date '+%F %T')] FAIL ${slug} rc=${RC} — see logs/${slug}.log" | tee -a batch.log
    FAILED=$((FAILED + 1))
  fi
done < "$LIST_FILE"

echo "[$(date '+%F %T')] batch finished: done=${DONE} failed=${FAILED}" | tee -a batch.log
