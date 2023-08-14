import pygame
import sys
from grid import Grid

WIDTH, HEIGHT = 300, 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game_grid = Grid()

game_grid.grid[0][0] = 1
game_grid.grid[3][5] = 4

game_grid.print_grid()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Draw
    screen.fill((44,44,127))
    game_grid.draw(screen)
    pygame.display.update()
    clock.tick(60)