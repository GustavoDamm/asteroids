from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import *
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt_clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT /2
    player = Player(x, y) # type: ignore
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt_tick = dt_clock.tick(60)
        dt = dt_tick/1000

if __name__ == "__main__":
    main()