import concurrent.futures
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'app'))
from model import Store
from serve import outcome
from web_support import Error


class PollTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.store = Store(self.temp.name)
        self.poll = self.store.create({'title': '聚餐', 'options': ['面馆', '火锅']})
        self.a, self.b = [item['id'] for item in self.poll['options']]

    def vote(self, name, option):
        return self.store.vote({'poll_id': self.poll['id'], 'participant': name, 'option_id': option})

    def test_unicode_casefold_replaces_existing_ballot(self):
        self.vote(' Straße ', self.a)
        result = self.vote('STRASSE', self.b)
        self.assertEqual((result['total_votes'], [x['count'] for x in result['options']]), (1, [0, 1]))
        with sqlite3.connect(self.store.path) as db:
            self.assertEqual(db.execute('SELECT participant_label FROM votes').fetchone()[0], 'STRASSE')

    def test_closed_vote_is_rejected_without_any_write_and_reopen_preserves(self):
        self.vote('小林', self.a)
        closed = self.store.status(self.poll['id'], 'closed')
        for name in ['小林', '小周']:
            with self.assertRaises(Error) as raised:
                self.vote(name, self.b)
            self.assertEqual((raised.exception.status, raised.exception.code), (409, 'poll_closed'))
        self.assertEqual(self.store.detail(self.poll['id']), closed)
        self.assertEqual(self.store.status(self.poll['id'], 'closed'), closed)
        self.store.status(self.poll['id'], 'open')
        self.assertEqual(self.vote('小林', self.b)['total_votes'], 1)

    def test_foreign_option_rejected_without_new_ballot(self):
        other = self.store.create({'title': '另一场', 'options': ['披萨', '寿司']})
        with self.assertRaises(Error) as raised:
            self.vote('小周', other['options'][0]['id'])
        self.assertEqual(raised.exception.code, 'invalid_option')
        self.assertEqual(self.store.detail(self.poll['id'])['total_votes'], 0)
        self.assertEqual(self.store.detail(other['id'])['total_votes'], 0)

    def test_tie_and_no_vote_do_not_invent_winner(self):
        self.assertIn('暂无投票', outcome(self.poll))
        self.vote('小林', self.a)
        result = self.vote('小周', self.b)
        self.assertEqual([x['count'] for x in result['options']], [1, 1])
        self.assertIn('并列：面馆、火锅，各 1 票', outcome(result))

    def test_invalid_create_is_atomic(self):
        for values in [[' A ', 'a'], ['面馆', ''], ['面馆'], ['面馆'] * 9, [1, '面馆']]:
            with self.assertRaises(Error) as raised:
                self.store.create({'title': '无效', 'options': values})
            self.assertEqual(raised.exception.code, 'invalid_options')
        self.assertEqual(len(self.store.listing()), 1)

    def test_demo_never_adds_to_existing_database(self):
        Store(self.temp.name, demo=True)
        self.assertEqual(self.store.listing(), [{'id': self.poll['id'], 'title': '聚餐', 'status': 'open'}])
        with tempfile.TemporaryDirectory() as new:
            first = Store(new, demo=True)
            before = first.listing()
            Store(new, demo=True)
            self.assertEqual(first.listing(), before)
            self.assertEqual(len(before), 1)

    def test_concurrent_same_alias_stays_one_person(self):
        def submit(index):
            self.vote('共享代号', self.a if index % 2 else self.b)
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(submit, range(24)))
        result = self.store.detail(self.poll['id'])
        self.assertEqual(result['total_votes'], 1)
        self.assertEqual(sorted(x['count'] for x in result['options']), [0, 1])


if __name__ == '__main__':
    unittest.main()
