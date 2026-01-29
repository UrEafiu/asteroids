import pygame
from constants import *
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            pass

        screen.fill("black")

        # To add 60 fps limitation for screen refresh.
        clock.tick(60)
        dt = clock.get_time() / 1000

        # To refresh.
        pygame.display.flip()

        # To make the pygame window exit when you click exit.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()