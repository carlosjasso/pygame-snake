from os import path
from modules.configuration import Configuration

def test_init():
    root = path.abspath(path.join(path.dirname(__file__), "..", ".."))
    result = Configuration()
    assert result
    assert result.paths
    assert len(result.paths) > 0
    assert result.paths["root"] == root
    assert result._config
    assert len(result._config.sections()) > 0

def test_get_window_props():
    result = Configuration().get_window_props()
    assert result
    assert len(result.size) == 2

def test_get_sprites_paths():
    result = Configuration().get_sprites_props()
    assert result
    assert len(result) > 0
