"""A source delivery must not recursively absorb its previous archive or user data."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

MODULE = Path(__file__).resolve().parents[1] / 'package_app.py'
spec = importlib.util.spec_from_file_location('package_app', MODULE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class AppPackageTests(unittest.TestCase):
    def test_inside_app_destination_is_safe_to_repeat(self):
        with tempfile.TemporaryDirectory() as tmp:
            app = Path(tmp) / 'sample'
            (app / 'data').mkdir(parents=True)
            (app / 'data/user.sqlite3').write_bytes(b'preserve user data')
            (app / 'serve.py').write_text('print("hello")\n')
            destination = app / 'source-package.zip'
            first = module.package(app, destination)
            again = module.package(app, destination)
            self.assertEqual(first['files'], again['files'])
            with zipfile.ZipFile(destination) as archive:
                self.assertEqual(archive.namelist(), ['sample/serve.py'])
                self.assertEqual(archive.read('sample/serve.py'), (app / 'serve.py').read_bytes())
            self.assertEqual((app / 'data/user.sqlite3').read_bytes(), b'preserve user data')
