from modules import Configuration
from modules import Window

if __name__ == "__main__": # entry point
    config = Configuration()
    window = Window(config)
    window.start()
