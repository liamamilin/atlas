import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))
spec = importlib.util.spec_from_file_location("budget_trial", ROOT / "app/serve.py")
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class BudgetTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.lib = app.Budget(Path(self.tmp.name))

    def test_exact_minor_units_and_invalid_amount(self):
        self.assertEqual(app.money("0.10") + app.money("0.20"), 30)
        for value in ("NaN", "Infinity", "1e2", "1.234", "-1", "", None, 1.2):
            with self.assertRaises(app.Error):
                app.money(value)

    def test_wrong_month_rolls_back_and_get_does_not_create(self):
        with app.connect(self.lib.path) as db:
            self.assertFalse(self.lib.state(db, "2026-10")["initialized"])
            self.assertEqual(db.execute("SELECT COUNT(*) FROM months").fetchone()[0], 0)
            self.lib.change(db, "/months/start", {"month": "2026-10"})
            cat, _ = self.lib.change(
                db, "/categories", {"month": "2026-10", "name": "食品", "amount": "10"}
            )
        with self.assertRaises(app.Error), app.connect(self.lib.path) as db:
            self.lib.change(
                db,
                "/expenses",
                {
                    "month": "2026-10",
                    "date": "2026-11-01",
                    "category_id": cat["id"],
                    "amount": "3.20",
                },
            )
        with app.connect(self.lib.path) as db:
            self.assertEqual(self.lib.state(db, "2026-10")["expenses"], [])

    def test_template_does_not_copy_expenses_or_change_existing_month(self):
        with app.connect(self.lib.path) as db:
            self.lib.change(db, "/months/start", {"month": "2026-10"})
            cat, _ = self.lib.change(
                db, "/categories", {"month": "2026-10", "name": "食品", "amount": "10"}
            )
            self.lib.change(
                db,
                "/expenses",
                {
                    "month": "2026-10",
                    "date": "2026-10-01",
                    "category_id": cat["id"],
                    "amount": "12.30",
                },
            )
            self.assertEqual(
                self.lib.state(db, "2026-10")["categories"][0]["remaining_minor"], -230
            )
            self.lib.change(db, "/template", {"month": "2026-10"})
            self.lib.change(db, "/months/start", {"month": "2026-11"})
            self.assertEqual(
                self.lib.state(db, "2026-11")["totals"]["remaining_minor"], 1000
            )
        with self.assertRaises(app.Error), app.connect(self.lib.path) as db:
            self.lib.change(db, "/months/start", {"month": "2026-10"})
        with app.connect(self.lib.path) as db:
            self.assertEqual(len(self.lib.state(db, "2026-10")["expenses"]), 1)


if __name__ == "__main__":
    unittest.main()
