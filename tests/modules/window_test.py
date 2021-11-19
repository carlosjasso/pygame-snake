import pytest
from modules.configuration import Configuration
from modules.window import Window

def test_init():
    result = Window(Configuration())
    assert result
    assert result._config

def test_init_pygame():
    try:
        window = Window(Configuration())
        window._init_pygame()
        assert window._sprites
        assert len(window._sprites) > 0
    except:
        pytest.fail("\n\tERROR: Something went wrong...")
