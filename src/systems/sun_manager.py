import pygame
import random

from src.settings import (
    WHITE,
    GRID_X,
    GRID_Y,
    GRID_COLS,
    GRID_ROWS,
    CELL_WIDTH,
    CELL_HEIGHT,
)
from src.entities.sun import Sun


class SunManager:
    def __init__(self):
        self.sun = 100
        self.sun_drops = []

        self.font = pygame.font.SysFont("Arial", 28, bold=True)
        self.spawn_interval = 8000
        self.last_spawn_time = pygame.time.get_ticks()

    def add_sun(self, amount):
        self.sun += amount

    def spend_sun(self, amount):
        if self.sun < amount:
            return False

        self.sun -= amount
        return True

    def spawn_sun(self, x, y):
        sun_drop = Sun(x, y)
        self.sun_drops.append(sun_drop)

    def collect_sun(self, position):
        for sun_drop in self.sun_drops[:]:
            if sun_drop.is_clicked(position):
                self.add_sun(sun_drop.value)
                self.sun_drops.remove(sun_drop)
                return True

    def draw(self, screen):
        text = self.font.render(f"Sun: {self.sun}", True, WHITE)
        screen.blit(text, (30, 30))

        for sun_drop in self.sun_drops:
            sun_drop.draw(screen)

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_spawn_time >= self.spawn_interval:
            x = random.randint(GRID_X + 25, GRID_Y + GRID_ROWS * CELL_HEIGHT - 25)
            y = random.randint(GRID_Y + 25, GRID_Y + GRID_ROWS * CELL_HEIGHT - 25)

            self.spawn_sun(x, y)
            self.last_spawn_time = current_time
