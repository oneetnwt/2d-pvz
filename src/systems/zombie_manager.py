import random
import pygame

from src.entities.zombie import Zombie
from src.settings import (
    GRID_ROWS,
    GRID_Y,
    CELL_HEIGHT,
    GRID_X,
    GRID_COLS,
    CELL_WIDTH,
)


class ZombieManager:
    def __init__(self):
        self.zombies = []

        self.spawn_interval = 10000
        self.last_spawn_time = pygame.time.get_ticks()

    def spawn_zombie(self):
        row = random.randint(0, GRID_ROWS - 1)

        x = GRID_X + GRID_COLS * CELL_WIDTH + 20
        y = GRID_Y + row * CELL_HEIGHT + 25

        zombie = Zombie(row, x, y)

        self.zombies.append(zombie)

    def update(self, delta_time, plant_manager):
        self.spawn_timer()

        for zombie in self.zombies:
            target_plant = None

            for plant in plant_manager.plants.values():
                if self.check_plant_collision(zombie, plant):
                    target_plant = plant
                    break

            if target_plant:
                zombie.is_attacking = True

                destroyed = zombie.attack(target_plant, delta_time)

                if destroyed:
                    plant_manager.remove_plant(target_plant.row, target_plant.col)

                    zombie.is_attacking = False

            else:
                zombie.is_attacking = False
                zombie.update(delta_time)

            self.zombies = [zombie for zombie in self.zombies if not zombie.is_dead()]

    def draw(self, screen):
        for zombie in self.zombies:
            zombie.draw(screen)

    def spawn_timer(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_spawn_time >= self.spawn_interval:
            self.spawn_zombie()
            self.last_spawn_time = current_time

    def check_plant_collision(self, zombie, plant):
        if zombie.row != plant.row:
            return False

        return zombie.rect.colliderect(plant.cell_rect)

    def has_reached_house(self):
        for zombie in self.zombies:
            if zombie.rect.right <= GRID_X:
                return True

        return False
