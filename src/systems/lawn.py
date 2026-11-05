import pygame

from src.settings import (
    GRID_ROWS,
    GRID_COLS,
    CELL_WIDTH,
    CELL_HEIGHT,
    GRID_X,
    GRID_Y,
    GREEN,
    LIGHT_GREEN,
    DARK_GREEN,
)


class Lawn:
    def __init__(self):
        self.grid = []

        self.create_grid()

    def create_grid(self):
        for row in range(GRID_ROWS):
            grid_row = []

            for col in range(GRID_COLS):
                x = GRID_X + col * CELL_WIDTH
                y = GRID_Y + row * CELL_HEIGHT

                rect = pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)

                grid_row.append(rect)

            self.grid.append(grid_row)

    def draw(self, screen):
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                color = LIGHT_GREEN if (row + col) % 2 == 0 else GREEN

                pygame.draw.rect(screen, color, self.grid[row][col])
                pygame.draw.rect(screen, color, self.grid[row][col], 1)

    def get_cell_at_position(self, position):
        for row_index, row in enumerate(self.grid):
            for col_index, rect in enumerate(row):
                if rect.collidepoint(position):
                    return row_index, col_index, rect

        return None
