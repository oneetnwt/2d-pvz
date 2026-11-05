import pygame


class Sun:
    def __init__(self, x, y, value=25):
        self.x = x
        self.y = y
        self.value = value
        self.radius = 22

        self.rect = pygame.Rect(
            x - self.radius, y - self.radius, self.radius * 2, self.radius * 2
        )

    def draw(self, screen):
        for angle in range(0, 360, 45):
            import math

            rad = math.radians(angle)

            start_x = self.x + math.cos(rad) * 18
            start_y = self.y + math.sin(rad) * 18

            end_x = self.x + math.cos(rad) * 28
            end_y = self.y + math.sin(rad) * 28

            pygame.draw.line(
                screen, (255, 190, 40), (start_x, start_y), (end_x, end_y), 4
            )

            pygame.draw.circle(screen, (255, 220, 70), (self.x, self.y), self.radius)

            pygame.draw.circle(
                screen, (255, 240, 130), (self.x, self.y), self.radius - 6
            )

    def is_clicked(self, position):
        return self.rect.collidepoint(position)
