from collections import namedtuple
from pathlib import Path
from configparser import ConfigParser
from .configuration_sprites import SpritesConfiguration
from .configuration_window import WindowConfiguration, WindowSize

Paths = namedtuple("Paths", ["ROOT", "PROJECT"])

class Configuration:
    paths : Paths
    parser : ConfigParser
    sprites : SpritesConfiguration
    window : WindowConfiguration

    def __init__(self):
        self.paths = self._build_paths()
        self.parser = self._build_config_parser()
        self.window = self._build_window_configuration()
        self.sprites = self._build_sprites_configuration()
    
    def _build_paths(self) -> Paths:
        root = [p for p in Path(__file__).parents if Path.exists(Path.joinpath(p, "setup.py"))][0]
        return Paths(
            ROOT = root.resolve(),
            PROJECT = Path.joinpath(root, "src/snake").resolve()
        )
    
    def _build_config_parser(self) -> ConfigParser:
        cfg_path = Path.joinpath(self.paths.PROJECT, "app.cfg")
        result = ConfigParser()
        result.read(cfg_path)
        return result
    
    def _build_window_configuration(self) -> WindowConfiguration:
        result = WindowConfiguration()
        result.WindowSize = WindowSize(
            WIDTH = int(self.get_section("WINDOW")["width"]),
            HEIGHT = int(self.get_section("WINDOW")["height"])
        )
        return result
    
    def _build_sprites_configuration(self) -> SpritesConfiguration:
        result = SpritesConfiguration()
        result.BLOCK_PATH = Path.joinpath(self.paths.ROOT, self.get_section("SPRITES")["block"])
        return result
    
    def get_section(self, section_name : str) -> dict[str, str]:
        """
        Returns a dictionary with the key/value pairs in the specified config parser section.
        """
        return dict(self.parser[section_name])
