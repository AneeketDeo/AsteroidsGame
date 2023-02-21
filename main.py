import random
import pygame
import pygame.mixer
import PlayerController
import EnemyController

# Initialize pygame and screen
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# background image
background_image = pygame.image.load('./images/bg2.jpg')

# pygame.display.update()

# music
pygame.mixer.init()
pygame.mixer.music.load('./music/asteroids-bg.mp3')
shoot_sound = pygame.mixer.Sound('./music/shoot.wav')
explosion_sound = pygame.mixer.Sound('./music/explosion.wav')

# Start playing the music in a continuous loop
pygame.mixer.music.play(-1)


# Set the clock speed
clock = pygame.time.Clock()

# Set the spawn timer
spawn_timer = pygame.time.get_ticks()
spawn_delay = 1000  # spawn a new enemy every 5 seconds

# set up the bullet variables
bullet_delay = 500  # milliseconds
last_bullet_time = 0

# Initialize spaceship and enemies
spaceship = PlayerController.Spaceship(400, 500, 5)


enemy_speed = 0.2



# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    # screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))

    # Move and draw spaceship and projectiles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship.x > 0:
        spaceship.move("left")
    if keys[pygame.K_RIGHT] and spaceship.x < SCREEN_WIDTH - PlayerController.spaceship_img.get_width():
        spaceship.move("right")
    if keys[pygame.K_UP] and spaceship.y > 0:
        spaceship.move("up")
    if keys[pygame.K_DOWN] and spaceship.y < SCREEN_HEIGHT - PlayerController.spaceship_img.get_height():
        spaceship.move("down")
    if keys[pygame.K_SPACE]:
        # check if enough time has elapsed since the last bullet was fired
        current_time = pygame.time.get_ticks()
        if current_time - last_bullet_time > bullet_delay:
            spaceship.shoot()
            shoot_sound.play()
            last_bullet_time = current_time
        

    spaceship.draw()

    for projectile in spaceship.projectiles:
        projectile.move()
        projectile.draw()


    # Check if it's time to spawn a new enemy
    for i in range(5):
        if pygame.time.get_ticks() - spawn_timer >= spawn_delay:
            # Spawn a new enemy
            new_enemy = EnemyController.Enemy(random.randint(0, 550), random.randint(0, 50), enemy_speed, EnemyController.enemy_img)
            EnemyController.Enemy.enemies.append(new_enemy)
            
            # Reset the spawn timer
            spawn_timer = pygame.time.get_ticks()
    
    for enemy in EnemyController.Enemy.enemies:
        enemy.move()
        enemy.draw()
        # for projectile in spaceship.projectiles:
        #     if enemy.check_collision(projectile.rect):
        #         print("enemy died")
        #         break

    # PlayerController.check_collision(EnemyController.Enemy.enemies, spaceship.projectiles)
    
     # Update the screen
    pygame.display.update()

    # Set the clock speed
    clock.tick(60)

# Quit the game
pygame.quit()
