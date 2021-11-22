from os import path
from configparser import ConfigParser, Error
from constants.error import ErrorMessage

class Configuration:
    def __init__(self) -> None:
        self.root_path = path.abspath(path.join(path.dirname(__file__), ".."))
        self._load_cfg_file()
    
    def _load_cfg_file(self) -> None:
        cfg_path = path.join(self.root_path, "app.cfg")
        if not path.exists(cfg_path):
            raise Error(ErrorMessage.CONFIG_NOT_FOUND)
        self._config = ConfigParser()
        self._config.read(cfg_path)
    
    def get_section(self, section_name : str):
        section = self._config[section_name]
        return section

    # def get_sprites_props(self) -> set[Sprite]:
    #     result = {}
    #     for s in self._config["SPRITES"]:
    #         result[s] = Sprite(name=s, path=self._config["SPRITES"][s])
    #     return result
