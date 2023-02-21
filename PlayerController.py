import pygame
import math
import EnemyController

# screen init
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load spaceship and projectile images
spaceship_img = pygame.image.load("./images/spaceship.png")
projectile_img = pygame.image.load("./images/projectile.png")


# Define class for spaceship
class Spaceship:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.projectiles = []

    def draw(self):
        screen.blit(spaceship_img, (self.x, self.y))

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        elif direction == "up":
            self.y -= self.speed
        elif direction == "down":
            self.y += self.speed


    def shoot(self):
        projectile = Projectile(self.x + 8, self.y - 5, 10, "up", projectile_img)
        self.projectiles.append(projectile)


# Define class for projectiles
class Projectile:
    def __init__(self, x, y, speed, direction, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alive = True

    def draw(self):
        screen.blit(projectile_img, (self.x, self.y))

    def move(self):
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed

# def check_collision(enemies, bullets):
#     for bullet in bullets:
#         for enemy in enemies:
#             if math.dist(bullet.pos, enemy.pos) < bullet.radius + enemy.radius:
#                 enemy.kill()
#                 enemies.remove(enemy)
#                 bullets.remove(bullet)
#                 print("inside check collision")