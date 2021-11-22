from collections import namedtuple
from os import path

import pygame
from models.configuration import Configuration
from models.sprite import Sprite

class Snake:
    def __init__(self, config : Configuration) -> None:
        self._load_props(config)
    
    def _load_props(self, config : Configuration) -> None:
        config_section = config.get_section("SPRITES")
        self.block = Sprite(
            name = "block",
            path = path.join(config.root_path, config_section["block"])
        )
        self.block.surface = pygame.image.load(self.block.path).convert()
