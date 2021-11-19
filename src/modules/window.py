import pygame
from pygame import Surface
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE
from modules.configuration import Configuration
# import window_props

class Window:
    def __init__(self, config : Configuration) -> None:
        pygame.init()
        self._config = config
        self.__init_pygame__()
        
    def __init_pygame__(self) -> None:
        props = self._config.get_window_props()
        surface : Surface = pygame.display.set_mode((props.width, props.height)) # set windows size in px
        surface.fill((110, 111, 5)) # set the window background color in RGB
        self.refresh()
        self.__load_sprites__()

    def __load_sprites__(self) -> None:
        pass
        # block = pygame.image.load(f"{config.ROOT_DIR}\\assets\\img\\block.jpg").convert()
    
    def refresh(self) -> None:
        pygame.display.flip() # refresh entide window
    
    def start(self) -> None:
        self._running = True

        while self._running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.stop()
                elif event.type == QUIT:
                    self.stop()

    def stop(self) -> None:
        self._running = False
