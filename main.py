import pygame
from constants import *
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    while True:
        log_state()

        for event in pygame.event.get():
            pass

        screen.fill("black")

        pygame.display.flip()

        # To make the pygame window exit when you click exit.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()