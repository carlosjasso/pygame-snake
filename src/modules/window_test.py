import unittest
from .configuration import Configuration
from .window import Window

class TestWindowModule(unittest.TestCase):
    def test_init(self):
        config = Configuration()
        actual = Window(config)
        self.assertTrue(actual)