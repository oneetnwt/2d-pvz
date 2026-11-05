from src.entities.projectile import Projectile


class ProjectileManager:
    def __init__(self):
        self.projectiles = []

    def spawn_projectiles(self, x, y):
        projectile = Projectile(x, y)
        self.projectiles.append(projectile)

    def update(self, delta_time, zombie_manager):
        for projectile in self.projectiles[:]:
            projectile.update(delta_time)

            for zombie in zombie_manager.zombies:
                if projectile.rect.colliderect(zombie.rect):
                    zombie.take_damage(projectile.damage)

                    self.projectiles.remove(projectile)
                    break

            self.projectiles = [
                projectile for projectile in self.projectiles if projectile.x < 1280
            ]

    def draw(self, screen):
        for projectile in self.projectiles:
            projectile.draw(screen)
