import pygame


class Zombie:
    def __init__(self, row, x, y):
        self.row = row
        self.x = x
        self.y = y

        self.width = 50
        self.height = 70

        self.speed = 20
        self.health = 100

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.is_attacking = False
        self.attack_damage = 10
        self.attack_interval = 1.0
        self.attack_timer = 0

    def update(self, delta_time):
        if not self.is_attacking:
            self.x -= self.speed * delta_time

        self.rect.x = int(self.x)

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 120, 90), self.rect, border_radius=8)
        pygame.draw.circle(
            screen, (130, 150, 110), (int(self.x + 25), int(self.y + 10)), 20
        )
        pygame.draw.circle(
            screen, (255, 255, 255), (int(self.x + 18), int(self.y + 7)), 5
        )
        pygame.draw.circle(
            screen, (255, 255, 255), (int(self.x + 32), int(self.y + 7)), 5
        )
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x + 18), int(self.y + 7)), 2)
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x + 32), int(self.y + 7)), 2)
        self.draw_health_bar(screen)

    def attack(self, plant, delta_time):
        self.attack_timer += delta_time

        if self.attack_timer >= self.attack_interval:
            destroyed = plant.take_damage(self.attack_damage)

            self.attack_timer = 0

            return destroyed

        return False

    def is_dead(self):
        return self.health <= 0

    def take_damage(self, amount):
        self.health -= amount

        if self.health < 0:
            self.health = 0

        return self.is_dead

    def draw_health_bar(self, screen):
        bar_width = 45
        bar_height = 5

        x = self.rect.centerx - bar_width // 2
        y = self.rect.top - 10

        # Background
        pygame.draw.rect(screen, (180, 50, 50), (x, y, bar_width, bar_height))

        # Current health
        health_width = int(bar_width * (self.health / 100))

        pygame.draw.rect(screen, (50, 200, 70), (x, y, health_width, bar_height))
