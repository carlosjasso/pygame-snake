from os import path
from configparser import ConfigParser
from models import WindowProps, Sprites, SpriteProps
from models import Constants, ErrorMessages

class Configuration:
    def __init__(self) -> None:
        self._load_paths()
        self._load_config()

    def _load_paths(self) -> None:
        root_path = path.abspath(path.join(path.dirname(__file__), ".."))
        self.paths = {
            "root": root_path,
        }

    def _load_config(self) -> None:
        config_path = path.join(self.paths["root"], Constants.CONFIG_FILE)
        if path.exists(config_path):
            self._config = ConfigParser()
            self._config.read(config_path)
        else:
            print(f"ERROR: {ErrorMessages.ERROR_CONFIG_NOT_FOUND}")

    def get_window_props(self) -> WindowProps:
        props = self._config["WINDOW"]
        return WindowProps(int(props["width"]), int(props["height"]))

    def get_sprites_props(self) -> Sprites:
        elements = {}
        for s in self._config["SPRITES"]:
            elements[s] = SpriteProps(name=s, path=self._config["SPRITES"][s])
        return elements
