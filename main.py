import pygame
from constants import *
from logger import log_state
from player import Player
from circleshape import CircleShape

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    clock = pygame.time.Clock()
    dt = 0

    # Instantiate "Player" object.
    new_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Game loop.
    while True:
        log_state()

        # To make the pygame window exit when you click exit.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # To add 60 fps limitation for screen refresh.
        clock.tick(60)
        dt = clock.get_time() / 1000

        # Draw player
        new_player.draw(screen)

        # Update player
        new_player.update(dt)
        new_player.draw(screen)

        # To refresh.
        pygame.display.flip()

if __name__ == "__main__":
    main()