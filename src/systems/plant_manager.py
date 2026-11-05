from src.entities.plant import Plant
from src.settings import PLANT_COST


class PlantManager:
    def __init__(self):
        self.plants = {}

    def place_plants(self, row, col, cell_rect, sun_manager):
        position = (row, col)

        if position in self.plants:
            return

        if not sun_manager.spend_sun(PLANT_COST):
            return False

        self.plants[position] = Plant(row, col, cell_rect)

        return True

    def draw(self, screen):
        for plant in self.plants.values():
            plant.draw(screen)

    def remove_plant(self, row, col):
        position = (row, col)

        if position in self.plants:
            del self.plants[position]

    def update(self, delta_time, zombie_manager, projectile_manager):
        for plant in self.plants.values():
            if plant.has_target(zombie_manager):
                plant.shoot(delta_time, projectile_manager)
