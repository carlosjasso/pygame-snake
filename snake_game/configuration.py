from configparser import ConfigParser
from pathlib import Path
from typing import NamedTuple

class WindowSize(NamedTuple):
    WIDTH : int
    HEIGHT : int

class DisplayConfiguration(NamedTuple):
    WINDOW_SIZE : WindowSize

class SpritesConfiguration(NamedTuple):
    BLOCK_PATH : Path
    APPLE_PATH : Path

class SpritesPaths(NamedTuple):
    ROOT : Path
    PROJECT : Path

class Configuration:
    paths : SpritesPaths
    parser : ConfigParser
    sprites : SpritesConfiguration
    window : DisplayConfiguration

    def __init__(self):
        self.paths = self._build_paths()
        self.parser = self._build_config_parser()
        self.window = self._build_window_configuration()
        self.sprites = self._build_sprites_configuration()
    
    def _build_paths(self) -> SpritesPaths:
        root = [p for p in Path(__file__).parents if Path.exists(Path.joinpath(p, "setup.py"))][0]
        return SpritesPaths(
            ROOT = root.resolve(),
            PROJECT = Path.joinpath(root, "snake_game").resolve()
        )
    
    def _build_config_parser(self) -> ConfigParser:
        cfg_path = Path.joinpath(self.paths.PROJECT, "game.cfg")
        result = ConfigParser()
        result.read(cfg_path)
        return result
    
    def _build_window_configuration(self) -> DisplayConfiguration:
        return DisplayConfiguration(
            WindowSize(
                WIDTH = int(self.get_section("DISPLAY")["width"]),
                HEIGHT = int(self.get_section("DISPLAY")["height"]))
        )
    
    def _build_sprites_configuration(self) -> SpritesConfiguration:
        return SpritesConfiguration(
            BLOCK_PATH = Path.joinpath(self.paths.ROOT, self.get_section("SPRITES")["block"]),
            APPLE_PATH = Path.joinpath(self.paths.ROOT, self.get_section("SPRITES")["apple"]),
        )
    
    def get_section(self, section_name : str) -> dict[str, str]:
        """
        Returns a dictionary with the key/value pairs in the specified config parser section.
        """
        return dict(self.parser[section_name])
