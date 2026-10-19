"""Pure fixtures for the fixed Docker network=none gate and no-fallback runner command."""
import importlib.util
import inspect
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("docker_acceptance_network_fixture", HERE / "docker_acceptance.py")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class NetworkNoneContractFixtures(unittest.TestCase):
    def test_only_none_network_without_published_ports_passes(self):
        runner.verify_network_none({"network_mode": "none", "port_bindings": {}, "effective_ports": {},
                                    "networks": {"none": {"IPAddress": ""}}})
        for meta in [
            {"network_mode": "bridge", "port_bindings": {}, "effective_ports": {}, "networks": {"bridge": {}}},
            {"network_mode": "none", "port_bindings": {"8000/tcp": []}, "effective_ports": {}, "networks": {"none": {}}},
            {"network_mode": "none", "port_bindings": {}, "effective_ports": {"8000/tcp": [{"HostIp": "127.0.0.1"}]}, "networks": {"none": {}}},
            {"network_mode": "none", "port_bindings": {}, "effective_ports": {}, "networks": {"bridge": {}}},
        ]:
            with self.subTest(meta=meta), self.assertRaises(RuntimeError):
                runner.verify_network_none(meta)

    def test_runner_uses_network_none_without_bridge_or_port_publish(self):
        source = inspect.getsource(runner.main)
        self.assertIn('"--network", "none"', source)
        self.assertNotIn('"--publish"', source)
        self.assertNotIn('docker("network", "create"', source)
        self.assertIn("verify_network_none(report[\"container_settings\"])", source)
        self.assertIn("verify_network_none(after_restart)", source)


if __name__ == "__main__":
    unittest.main()
