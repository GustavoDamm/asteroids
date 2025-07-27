from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import *
from player import Player
from asteroid import *
import pygame

def main():
    #Initialize
    pygame.init()

    #Create screen for resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Inside clock tick for fps
    dt_clock = pygame.time.Clock()
    dt = 0

    #Create group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #Player container
    Player.containers = (updatable, drawable)

    #Asteroid container
    Asteroid.containers = (asteroids, updatable, drawable)

    #AsteroidField container
    AsteroidField.containers = (updatable,)

    #Create player position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT /2
    player = Player(x, y)

    #Create Asteroid Field
    asteroid_field = AsteroidField()

    #Start game loop
    while True:
        #Check if game is closed on clicking X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Update player based on internal clock
        updatable.update(dt)

        #Loop on drawables to draw them individually


        #Render Screen
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        #Set internal clock for 60 FPS
        dt_tick = dt_clock.tick(60)
        dt = dt_tick/1000

if __name__ == "__main__":
    main()