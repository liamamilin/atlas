"""Read only owned OpenCode sessions to audit actual first user input."""

import hashlib
import json
import os
import shutil
import subprocess
import sys
from prepare import HERE, ROOT, save

sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from privacy import redact_text


def main():
    records = {}
    for summary in sorted(
        (HERE / "runs").glob("*/*/*/attempt-*/scenario-review/cli-summary.json")
    ):
        stage = summary.parent
        cli = json.loads(summary.read_text())
        assert len(cli["session_ids"]) == 1
        sid = cli["session_ids"][0]
        receipt = stage / "actual-user-input.json"
        previous = json.loads(receipt.read_text()) if receipt.exists() else None
        if previous and "assistant_usage_records" in previous:
            records[str(stage.relative_to(HERE))] = json.loads(receipt.read_text())
            continue
        env = dict(os.environ)
        for key in [
            "OPENCODE_CONFIG",
            "OPENCODE_CONFIG_CONTENT",
            "OPENCODE_CONFIG_DIR",
        ]:
            env.pop(key, None)
        env.update(PWD=str(stage), OPENCODE_CONFIG=str(stage / "opencode.json"))
        p = subprocess.run(
            [shutil.which("opencode"), "session", "export", "--standalone", sid],
            cwd=stage,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60,
        )
        if p.returncode:
            save(
                receipt,
                {
                    "status": "audit_export_failed",
                    "error": redact_text(p.stderr.decode(errors="replace"))[-600:],
                },
            )
            continue
        session = json.loads(p.stdout)
        users = [m for m in session["messages"] if m.get("type") == "user"]
        assert len(users) == 1, (
            "Unexpected extra user messages in isolated author session"
        )
        text = users[0]["text"]
        if previous and previous.get("actual_text_sha256"):
            assert (
                hashlib.sha256(text.encode()).hexdigest()
                == previous["actual_text_sha256"]
            )
        marker = "import runpy,sys,time\n"
        a = text.find(marker)
        b = text.find("run_name='__main__')", a)
        extra = text[a : b + len("run_name='__main__')")] if a >= 0 and b >= a else None
        (stage / "actual-user-input.txt").write_text(redact_text(text))
        row = {
            "status": "read_owned_session",
            "session_id": sid,
            "user_messages": len(users),
            "actual_text_characters": len(text),
            "actual_text_utf8_bytes": len(text.encode()),
            "actual_text_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "source": "OpenCode session export first user message; full redacted text stored beside this receipt",
            "host_heredoc_script_present": extra is not None,
            "host_heredoc_script_character_offset": a if extra else None,
            "host_heredoc_script_sha256": hashlib.sha256(extra.encode()).hexdigest()
            if extra
            else None,
            "host_heredoc_script_characters": len(extra) if extra else 0,
            "native_template_file_tag_present": '<file name="FULL_TEMPLATE.md">'
            in text,
            "limits": "Stored session input is not a guarantee of final provider preprocessing/context exposure.",
            "assistant_usage_records": [
                {
                    key: message.get(key)
                    for key in ["id", "finish", "rawFinish", "tokens", "model"]
                }
                for message in session["messages"]
                if message.get("type") == "assistant"
            ],
            "usage_limits": "Session-export fields recover terminal usage absent from CLI step_finish events. They overlap event usage; never add both. Not an invoice or unique billed-token total.",
        }
        save(receipt, row)
        records[str(stage.relative_to(HERE))] = row
    save(
        HERE / "actual-input-audit.json",
        {"status": "all_finished_author_sessions_audited", "records": records},
    )
    for key, row in records.items():
        print(
            key,
            "stdin_script",
            row.get("host_heredoc_script_present"),
            "native_file",
            row.get("native_template_file_tag_present"),
        )


if __name__ == "__main__":
    main()
