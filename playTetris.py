import pygame
import sys

WIDTH, HEIGHT = 300, 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Draw
    screen.fill((255,255,255))
    pygame.display.update()
    clock.tick(60)