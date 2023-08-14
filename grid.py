import pygame
class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_cell_colors()
    
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def get_cell_colors(self):

        red = (235, 15, 15)
        blue = (15, 65, 215)
        green = (50, 230, 20)
        yellow = (240, 230, 0)
        cyan = (20, 200, 200)
        purple = (170, 0, 250)
        orange = (230, 110, 20)
        
        return [red, blue, green, yellow, cyan, purple, orange]

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 1, row*self.cell_size + 1,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)