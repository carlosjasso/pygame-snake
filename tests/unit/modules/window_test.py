from models.configuration import Configuration
from modules.window import Window

def test_init():
    actual = Window(Configuration())
    assert actual
    assert actual.surface.get_width() > 0  \
        and actual.surface.get_height() > 0
    assert len(actual.background_color) == 3