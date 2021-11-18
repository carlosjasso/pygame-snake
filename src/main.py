import pygame
from pygame import Surface
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE
from models.configuration import Configuration

if __name__ == "__main__": # entry point
    config = Configuration()

    pygame.init() # Init the module

    surface : Surface = pygame.display.set_mode((500, 500)) # set windows size in px
    surface.fill((110, 111, 5)) # set the window color in RGB

    block = pygame.image.load(f"{config.ROOT_DIR}\\assets\\img\\block.jpg").convert()

    pygame.display.flip() # refresh entide window

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False