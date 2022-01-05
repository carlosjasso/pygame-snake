from configparser import ConfigParser
from pathlib import Path
from utils.types import GameConfiguration, WindowSize, DisplayConfiguration, SpritesConfiguration, SpritesPaths

class Configuration:
    #region attributes & Properties
    _parser : ConfigParser
    paths : SpritesPaths
    game : GameConfiguration
    window : DisplayConfiguration
    sprites : SpritesConfiguration
    #endregion

    #region Init
    def __init__(self):
        self.paths = self._build_paths()
        self._parser = self._build_config_parser()
        self.game = self._build_game_configuration()
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

    def _build_game_configuration(self) -> GameConfiguration:
        return GameConfiguration(
            DELAY = float(self._get_section("GAME")["delay"]),
            DELAY_MULTIPLIER = float(self._get_section("GAME")["delaymultiplier"])
        )

    def _build_window_configuration(self) -> DisplayConfiguration:
        return DisplayConfiguration(
            WindowSize(
                WIDTH = int(self._get_section("DISPLAY")["width"]),
                HEIGHT = int(self._get_section("DISPLAY")["height"]))
        )

    def _build_sprites_configuration(self) -> SpritesConfiguration:
        return SpritesConfiguration(
            BLOCK_PATH = Path.joinpath(self.paths.ROOT, self._get_section("SPRITES")["block"]),
            APPLE_PATH = Path.joinpath(self.paths.ROOT, self._get_section("SPRITES")["apple"]),
        )
    #endregion

    #region helpers
    def _get_section(self, section_name : str) -> dict[str, str]:
        """
        Returns a dictionary with the key/value pairs in the specified config parser section.
        """
        return dict(self._parser[section_name])
    #endregion
