import pygame


class Plant:
    def __init__(self, row, col, cell_rect):
        self.row = row
        self.col = col
        self.cell_rect = cell_rect
        self.health = 100
        self.shoot_interval = 1.5
        self.shoot_timer = 0

    def draw(self, screen):
        center_x = self.cell_rect.centerx
        center_y = self.cell_rect.centery

        pygame.draw.line(
            screen,
            (40, 120, 45),
            (center_x, center_y + 10),
            (center_x, center_y + 35),
            6,
        )

        pygame.draw.ellipse(
            screen, (60, 150, 60), (center_x - 28, center_y + 15, 25, 12)
        )

        pygame.draw.ellipse(
            screen, (60, 150, 60), (center_x + 3, center_y + 15, 25, 12)
        )

        pygame.draw.circle(screen, (90, 180, 70), (center_x, center_y - 5), 22)
        pygame.draw.circle(screen, (255, 255, 255), (center_x - 7, center_y - 10), 4)
        pygame.draw.circle(screen, (255, 255, 255), (center_x + 7, center_y - 10), 4)
        pygame.draw.circle(screen, (30, 30, 30), (center_x - 7, center_y - 10), 2)
        pygame.draw.circle(screen, (30, 30, 30), (center_x + 7, center_y - 10), 2)

        self.draw_health_bar(screen)

    def take_damage(self, amount):
        self.health -= amount

        if self.health < 0:
            self.health = 0

        return self.health <= 0

    def is_destroyed(self):
        return self.health <= 0

    def draw_health_bar(self, screen):
        bar_width = 50
        bar_height = 6

        x = self.cell_rect.centerx - bar_width
        y = self.cell_rect.centery + 40

        pygame.draw.rect(screen, (180, 50, 50), (x, y, bar_width, bar_height))

        health_width = int(bar_width * (self.health / 100))

        pygame.draw.rect(screen, (50, 200, 70), (x, y, health_width, bar_height))

    def shoot(self, delta_time, projectile_manager):
        self.shoot_timer += delta_time

        if self.shoot_timer >= self.shoot_interval:
            center_x = self.cell_rect.centerx
            center_y = self.cell_rect.centery - 5

            projectile_manager.spawn_projectiles(center_x + 20, center_y)

            self.shoot_timer = 0

    def has_target(self, zombie_manager):
        for zombie in zombie_manager.zombies:
            if zombie.row == self.row:
                return True

        return False
