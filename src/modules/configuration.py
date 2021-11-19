from os import path
from configparser import ConfigParser
from ..models import constants
from ..models.types import WindowProps

class Configuration:
    def __init__(self) -> None:
        self.__load_paths__()
        self.__load_config__()

    def __load_paths__(self) -> None:
        root_path = path.abspath(path.join(path.dirname(__file__), "..", ".."))
        self.paths = {
            "root": root_path,
            "src": path.join(root_path, "src")
        }

    def __load_config__(self) -> None:
        config_path = path.join(self.paths["src"], constants.Common.CONFIG_FILE)
        if path.exists(config_path):
            self._config = ConfigParser()
            self._config.read(config_path)
        else:
            print(f"ERROR: {constants.Errors.ERROR_CONFIG_NOT_FOUND}")

    def get_window_props(self) -> WindowProps:
        props = self._config["WINDOW"]
        return WindowProps(int(props["Width"]), int(props["Height"]))
