import pygame


class Projectile:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

        self.radius = 8
        self.speed = 350
        self.damage = 25

        self.rect = pygame.Rect(
            int(self.x - self.radius),
            int(self.y - self.radius),
            self.radius * 2,
            self.radius * 2,
        )

    def update(self, delta_time):
        self.x += self.speed * delta_time

        self.rect.center = (int(self.x), int(self.y))

    def draw(self, screen):
        pygame.draw.circle(
            screen, (80, 200, 70), (int(self.x), int(self.y)), self.radius
        )

        pygame.draw.circle(
            screen, (140, 240, 100), (int(self.x), int(self.y)), self.radius - 3
        )
