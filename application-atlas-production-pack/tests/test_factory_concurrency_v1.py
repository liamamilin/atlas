"""SQLite WAL concurrency regressions for independently initialized factory stores."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import threading
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.budget import BudgetLedger
from template_factory.store import FactoryStore

PACK = Path(__file__).resolve().parents[1]


class FactoryConcurrencyV1Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        shutil.copy(PACK / "mvp_apps.json", self.pack / "mvp_apps.json")
        (self.pack / "atlas").mkdir()
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
            con.execute("INSERT INTO leaf VALUES('bookmark-manager','Bookmarks','书签','Save links','Links')")
        self.db_root = self.root / "factory"
        self.store = FactoryStore(self.db_root, self.pack)

    def tearDown(self):
        self.temp.cleanup()

    def _scenario(self, name):
        return self.store.save_scenario({
            "leaf": "bookmark-manager", "name": name, "audience": "Personal",
            "objective": "Save links", "workflow": ["save", "read"],
            "acceptance": ["Saved links remain"], "status": "ready",
        })

    def test_wal_writer_commit_does_not_block_or_change_open_reader_snapshot(self):
        self._scenario("Existing scenario")
        with self.store.connect() as reader:
            self.assertEqual(reader.execute("PRAGMA journal_mode").fetchone()[0].lower(), "wal")
            reader.execute("BEGIN")
            before = reader.execute("SELECT count(*) FROM scenario").fetchone()[0]
            outcome = []
            finished = threading.Event()

            def writer():
                try:
                    self._scenario("Concurrent committed scenario")
                    outcome.append("committed")
                except Exception as error:  # surface worker-thread failure to the test
                    outcome.append(error)
                finally:
                    finished.set()

            thread = threading.Thread(target=writer)
            thread.start()
            self.assertTrue(finished.wait(5), "WAL writer was blocked by the open reader")
            thread.join(timeout=5)
            self.assertFalse(thread.is_alive())
            self.assertEqual(outcome, ["committed"])
            # A reader transaction retains its original snapshot after writer commit.
            self.assertEqual(reader.execute("SELECT count(*) FROM scenario").fetchone()[0], before)

        with self.store.connect() as reader:
            self.assertEqual(reader.execute("SELECT count(*) FROM scenario").fetchone()[0], before + 1)

    def test_reinitialization_and_budget_snapshots_survive_concurrent_threads(self):
        expected = [self._scenario(f"Initial {index}")["id"] for index in range(5)]
        barrier = threading.Barrier(8)

        def read_reinitialized_store(index):
            store = FactoryStore(self.db_root, self.pack)
            ledger = BudgetLedger(store, campaign_id="concurrency-regression")
            barrier.wait(timeout=10)
            for _ in range(6):
                with store.connect() as con:
                    ids = [row[0] for row in con.execute("SELECT id FROM scenario ORDER BY id")]
                status = ledger.status()
                if not set(expected).issubset(ids):
                    raise AssertionError("scenario rows were lost during repeated initialization")
                if not isinstance(status, dict):
                    raise AssertionError("budget snapshot was not returned")
            return len(ids)

        with ThreadPoolExecutor(max_workers=8) as pool:
            counts = list(pool.map(read_reinitialized_store, range(8)))
        self.assertEqual(counts, [5] * 8)
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT count(*) FROM scenario").fetchone()[0], 5)
            self.assertEqual(con.execute("PRAGMA journal_mode").fetchone()[0].lower(), "wal")


if __name__ == "__main__":
    unittest.main()
