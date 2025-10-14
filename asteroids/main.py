import pygame
from constants import *



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    i = 0
    while i < 1:
        screen.fill(0)
        pygame.display.flip()


if __name__ == "__main__":
    main()
