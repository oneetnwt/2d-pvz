import pygame

from src.settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    FPS,
    GREEN,
    GAME_RUNNING,
    GAME_OVER,
    GAME_MENU,
)
from src.systems.lawn import Lawn
from src.systems.plant_manager import PlantManager
from src.systems.sun_manager import SunManager
from src.systems.zombie_manager import ZombieManager
from src.systems.projectile_manager import ProjectileManager


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption(WINDOW_TITLE)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.clock = pygame.time.Clock()

        self.game_state = GAME_MENU
        self.running = True
        self.lawn = Lawn()
        self.plant_manager = PlantManager()
        self.sun_manager = SunManager()
        self.zombie_manager = ZombieManager()
        self.projectile_manager = ProjectileManager()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    collected = self.sun_manager.collect_sun(event.pos)

                    if not collected:
                        cell = self.lawn.get_cell_at_position(event.pos)

                        if cell:
                            row, col, rect = cell

                            self.plant_manager.place_plants(
                                row, col, rect, self.sun_manager
                            )
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if self.game_state == GAME_OVER:
                        self.reset_game()

    def update(self, delta_time):
        self.sun_manager.update()
        self.zombie_manager.update(delta_time, self.plant_manager)
        self.projectile_manager.update(delta_time, self.zombie_manager)
        self.plant_manager.update(
            delta_time, self.zombie_manager, self.projectile_manager
        )

        if self.zombie_manager.has_reached_house():
            self.game_state = GAME_OVER

    def render(self, delta_time):
        self.screen.fill(GREEN)

        self.lawn.draw(self.screen)
        self.plant_manager.draw(self.screen)
        self.sun_manager.draw(self.screen)
        self.zombie_manager.draw(self.screen)
        self.projectile_manager.draw(self.screen)
        if self.game_state == GAME_OVER:
            self.draw_game_over()

        pygame.display.flip()

    def run(self):
        while self.running:
            delta_time = self.clock.tick(FPS) / 1000.0

            self.handle_events()
            self.update(delta_time)
            self.render(self.screen)

        pygame.quit()

    def draw_game_over(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)

        overlay.fill((0, 0, 0, 170))
        self.screen.blit(overlay, (0, 0))

        font = pygame.font.SysFont("Arial", 64, bold=True)

        text = font.render("GAME OVER", True, (255, 70, 70))

        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        self.screen.blit(text, text_rect)
        restart_font = pygame.font.SysFont("Arial", 28)

        restart_text = restart_font.render("Press R to Restart", True, (255, 255, 255))

        restart_rect = restart_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70)
        )

        self.screen.blit(restart_text, restart_rect)

    def reset_game(self):
        self.game_state = GAME_RUNNING

        self.plant_manager = PlantManager()
        self.sun_manager = SunManager()
        self.zombie_manager = ZombieManager()
        self.projectile_manager = ProjectileManager()
