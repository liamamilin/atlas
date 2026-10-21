"""Local poll storage. Counts are derived; a participant owns one row per poll."""

from pathlib import Path
import uuid

from web_support import Error, connect


class Store:
    def __init__(self, data_dir, demo=False):
        directory = Path(data_dir)
        directory.mkdir(parents=True, exist_ok=True)
        self.path = directory / "dinner-poll.sqlite3"
        new_database = not self.path.exists()
        with connect(self.path) as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS polls (
                    id TEXT PRIMARY KEY, title TEXT NOT NULL,
                    status TEXT NOT NULL CHECK(status IN ('open','closed'))
                );
                CREATE TABLE IF NOT EXISTS options (
                    id TEXT PRIMARY KEY, poll_id TEXT NOT NULL REFERENCES polls(id),
                    label TEXT NOT NULL, position INTEGER NOT NULL,
                    UNIQUE(poll_id, id)
                );
                CREATE TABLE IF NOT EXISTS votes (
                    poll_id TEXT NOT NULL REFERENCES polls(id),
                    participant_key TEXT NOT NULL, participant_label TEXT NOT NULL,
                    option_id TEXT NOT NULL,
                    PRIMARY KEY(poll_id, participant_key),
                    FOREIGN KEY(poll_id, option_id) REFERENCES options(poll_id,id)
                );
            """)
        if demo and new_database:
            poll = self.create({"title": "周五聚餐，去哪里？", "options": ["巷口面馆", "山城火锅", "街角披萨"]})
            self.vote({"poll_id": poll["id"], "participant": "小林", "option_id": poll["options"][0]["id"]})
            self.vote({"poll_id": poll["id"], "participant": "小周", "option_id": poll["options"][1]["id"]})

    @staticmethod
    def _text(value, minimum, maximum, code, message):
        if not isinstance(value, str) or not minimum <= len(value.strip()) <= maximum:
            raise Error(code, message)
        return value.strip()

    def listing(self):
        with connect(self.path) as db:
            return [dict(row) for row in db.execute("SELECT id,title,status FROM polls ORDER BY rowid DESC")]

    @staticmethod
    def _detail(db, poll_id):
        if not isinstance(poll_id, str):
            raise Error("not_found", "找不到这个投票。", 404)
        row = db.execute("SELECT id,title,status FROM polls WHERE id=?", (poll_id,)).fetchone()
        if row is None:
            raise Error("not_found", "找不到这个投票。", 404)
        poll = dict(row)
        poll["options"] = [dict(option) for option in db.execute("""
            SELECT o.id,o.label,COUNT(v.participant_key) AS count
            FROM options o LEFT JOIN votes v ON v.poll_id=o.poll_id AND v.option_id=o.id
            WHERE o.poll_id=? GROUP BY o.id ORDER BY o.position
        """, (poll_id,))]
        poll["total_votes"] = sum(option["count"] for option in poll["options"])
        return poll

    def detail(self, poll_id):
        with connect(self.path) as db:
            return self._detail(db, poll_id)

    def create(self, data):
        title = self._text(data.get("title"), 1, 160, "invalid_title", "问题须为 1–160 个字符。")
        raw = data.get("options")
        if not isinstance(raw, list) or not 2 <= len(raw) <= 8:
            raise Error("invalid_options", "请填写 2–8 个地点，每行一个。")
        labels = [self._text(value, 1, 80, "invalid_options", "每个地点须为 1–80 个字符，不能留空。") for value in raw]
        if len({label.casefold() for label in labels}) != len(labels):
            raise Error("invalid_options", "地点不能重复（忽略首尾空格和字母大小写）。")
        poll_id = uuid.uuid4().hex
        with connect(self.path) as db:
            db.execute("INSERT INTO polls VALUES (?,?,'open')", (poll_id, title))
            db.executemany("INSERT INTO options VALUES (?,?,?,?)", [(uuid.uuid4().hex, poll_id, label, position) for position, label in enumerate(labels)])
            return self._detail(db, poll_id)

    def vote(self, data):
        participant = self._text(data.get("participant"), 1, 40, "invalid_participant", "请填写 1–40 个字符的代号。")
        with connect(self.path) as db:
            # Lock before checking status: close and vote cannot interleave.
            db.execute("BEGIN IMMEDIATE")
            poll = self._detail(db, data.get("poll_id"))
            if poll["status"] == "closed":
                raise Error("poll_closed", "投票已结束，不能投票或改票；请先重开。", 409)
            option_id = data.get("option_id")
            if not isinstance(option_id, str) or option_id not in {option["id"] for option in poll["options"]}:
                raise Error("invalid_option", "请选择属于本次投票的一个地点。")
            db.execute("""INSERT INTO votes VALUES (?,?,?,?)
                ON CONFLICT(poll_id,participant_key) DO UPDATE SET
                participant_label=excluded.participant_label,option_id=excluded.option_id
            """, (poll["id"], participant.casefold(), participant, option_id))
            return self._detail(db, poll["id"])

    def status(self, poll_id, target):
        if target not in ("open", "closed"):
            raise ValueError("unsupported poll status")
        with connect(self.path) as db:
            db.execute("BEGIN IMMEDIATE")
            self._detail(db, poll_id)
            db.execute("UPDATE polls SET status=? WHERE id=?", (target, poll_id))
            return self._detail(db, poll_id)
