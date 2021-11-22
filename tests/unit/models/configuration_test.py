from os import path
from models.configuration import Configuration

def test_init():
    expected = path.abspath(path.join(path.dirname(__file__), "..", "..", ".."))
    actual = Configuration()
    assert actual
    assert actual.root_path == expected
    assert len(actual._config.sections()) > 0

def test_get_section():
    config = Configuration()
    property_names = ["WINDOW", "SPRITES"]
    actual = {p:config.get_section(p) for p in property_names}
    assert len(actual) > 0
    for p in property_names: assert actual[p]