import pygame
import math

# screen init
screen = pygame.display.set_mode((800, 600))

# Load spaceship and enemy images
enemy_img = pygame.image.load("./images/enemy.png")

# Define class for enemy
class Enemy:
    enemies = []
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alive = True
    

    def draw(self):
        screen.blit(enemy_img, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 50, 50))
        

    def move(self):
        self.y += self.speed

    
    
    def kill(self):
        if not self.alive:
            # remove the enemy from the list of enemies
            enemies.remove(self)

    # def spawn(self, count):
    #     for i in range(count):
    #         enemies.append(Enemy(self.x, self.y, self.speed))