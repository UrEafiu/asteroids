import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    clock = pygame.time.Clock()
    dt = 0

    # Creating groups for elements of the game and putting the elements in relevant groups.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable) #Adds the player objects to both groups.
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Instantiate "Player" object.
    new_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Instantiate "Asteroid Field"
    field = AsteroidField()

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

        # Draw elements in the drawable group.
        for element in drawable:
            element.draw(screen)

        # Update elements in the updatable group.
        updatable.update(dt)

        # Draw elements in the drawable group.
        for element in drawable:
            element.draw(screen)

        # To refresh.
        pygame.display.flip()

if __name__ == "__main__":
    main()