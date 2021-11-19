import unittest
from src.modules.configuration import Configuration
from src.modules.window import Window

class TestWindowModule(unittest.TestCase):
    def test_init(self):
        config = Configuration()
        actual = Window(config)
        self.assertTrue(actual)