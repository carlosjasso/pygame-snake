import unittest
from os import path
from .configuration import Configuration

class TestConfigurationModule(unittest.TestCase):
    def test_init(self):
        actual = Configuration()
        self.assertTrue(actual)
        self.assertEqual(path.basename(actual.paths["root"]), "pygame-snake")
        self.assertTrue(actual._config)

    def test_window(self):
        config = Configuration()
        actual = config.get_window_props()
        self.assertTrue(actual)
        self.assertTrue(actual.width)
        self.assertTrue(actual.height)