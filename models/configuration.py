from os import path
from configparser import ConfigParser

class Configuration:
    root_path : str
    _config : ConfigParser

    def __init__(self) -> None:
        self.root_path = path.abspath(path.join(path.dirname(__file__), ".."))
        self._load_cfg_file()
    
    def _load_cfg_file(self) -> None:
        cfg_path = path.join(self.root_path, "app.cfg")
        self._config = ConfigParser()
        self._config.read(cfg_path)
    
    def get_section(self, section_name : str):
        """
        Returns a dictionary with the key/value pairs in the specified section.
        """
        return dict(self._config[section_name])
