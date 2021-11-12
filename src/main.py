from os import path
import pygame
from pygame import Surface
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE

ROOT_DIR = path.abspath(path.join(path.dirname(__file__), ".."))

if __name__ == "__main__": # entry point
    pygame.init() # Init the module

    surface : Surface = pygame.display.set_mode((500, 500)) # set windows size in px
    surface.fill((110, 111, 5)) # set the window color in RGB

    block = pygame.image.load(f"{ROOT_DIR}\\assets\\img\\block.jpg").convert()

    pygame.display.flip() # refresh entide window

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False