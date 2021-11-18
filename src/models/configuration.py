from os import path

class Configuration:
    def __init__(self) -> None:
        self.ROOT_DIR = path.abspath(path.join(path.dirname(__file__), ".."))

