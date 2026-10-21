from pathlib import Path
from types import SimpleNamespace
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'app'))
from model import Store
from serve import App


class RenderingTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.store = Store(temporary.name)
        self.handler = object.__new__(App)
        self.handler.server = SimpleNamespace(store=self.store)
        self.handler.data = {}
        self.handler.query = {}
        self.poll = self.store.create({'title': '<script>聚餐</script>', 'options': ['面馆 <A>', '火锅 & B']})

    def test_invalid_form_retains_escaped_participant_and_selected_option(self):
        selected = self.poll['options'][1]['id']
        self.handler.data = {'participant': '\"<小林>', 'option_id': selected}
        html = self.handler.detail_page(self.poll['id'], '请检查输入', True)
        self.assertIn('value="&quot;&lt;小林&gt;"', html)
        self.assertIn(f'value="{selected}" checked required', html)
        self.assertIn('role="alert"', html)
        self.assertNotIn('<script>聚餐</script>', html)
        self.assertIn('&lt;script&gt;聚餐&lt;/script&gt;', html)
        self.assertIn('火锅 &amp; B', html)

    def test_close_and_reopen_show_actionable_status(self):
        self.store.status(self.poll['id'], 'closed')
        html = self.handler.detail_page(self.poll['id'], '投票已结束，结果已冻结。')
        self.assertIn('<fieldset disabled>', html)
        self.assertIn('重开后才能投票或改票', html)
        self.assertIn('action="/reopen"', html)
        self.assertIn('role="status"', html)
        self.store.status(self.poll['id'], 'open')
        html = self.handler.detail_page(self.poll['id'], '投票已重开，可以继续投票或改票。')
        self.assertNotIn('<fieldset disabled>', html)
        self.assertIn('action="/close"', html)
        self.assertIn('同机共享，代号不是身份认证。', html)

    def test_create_error_keeps_all_lines_and_title(self):
        self.handler.data = {'title': '保留 <问题>', 'options': '面馆\n\n火锅'}
        html = self.handler.home('地点不能为空', True)
        self.assertIn('value="保留 &lt;问题&gt;"', html)
        self.assertIn('>面馆\n\n火锅</textarea>', html)


if __name__ == '__main__':
    unittest.main()
