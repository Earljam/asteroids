import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Asteroid.containers = (all_asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      return
          screen.fill("black")
          for i in drawable:
                i.draw(screen)
          for i in updatable:
                i.update(dt)
          #player.draw(screen)
          #player.update(dt)
          pygame.display.flip()
          dt = clock.tick(60) / 1000
          

if __name__ == "__main__":
        main()
