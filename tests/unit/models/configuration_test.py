from pathlib import Path
from src.snake.models.configuration import Configuration

def test_init():
    expected_root = Path(__file__).parent.parent.parent.parent
    actual = Configuration()
    assert actual.paths.ROOT == expected_root
    for p in actual.paths: assert Path.exists(p)
    assert type(actual.window.WindowSize.WIDTH) == int \
        and type(actual.window.WindowSize.HEIGHT) == int
    assert Path.exists(actual.sprites.BLOCK_PATH)

def test_get_section():
    config = Configuration()
    property_names = ["WINDOW", "SPRITES"]
    actual = {p:config.get_section(p) for p in property_names}
    assert len(actual) > 0
    for p in property_names: assert actual[p]