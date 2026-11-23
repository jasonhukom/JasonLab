import pygame
from sys import exit
import random

title = "Mushrams: Power Up!"
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(title)
clock = pygame.time.Clock()
# D:/valis/Downloads/pygame
# Fonts
fontbigfish = pygame.font.Font('./images/Bigfish.ttf', 50)
fontrushblade = pygame.font.Font('./images/font/rushlade/Rushblade.ttf', 100)
fontracemaster = pygame.font.Font('./images/font/racemaster/Race Master.otf', 50)

# Assets
enemy_x = 650
enemy_y = 300
title_timer = 3000  # 3 seconds in milliseconds

sky_surface = pygame.image.load('./images/sky.png')
ground_surface = pygame.image.load('./images/ground.png')
txt_surface = fontrushblade.render('MUSHRAMS', False, "Black")
txt_surface2 = fontracemaster.render('Power Up!', False, "Black")

enemy_surface = pygame.image.load('./images/enemy.png')
enemy_surface_mirrored = pygame.transform.flip(enemy_surface, True, False)

# Start time
start_time = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Background
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 100))

    # Countdown title (only show if less than 3 sec passed)
    current_time = pygame.time.get_ticks()
    if current_time - start_time < title_timer:
        screen.blit(txt_surface, (100, 50))
        screen.blit(txt_surface2, (100, 150))
    
    # Enemy movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        screen.blit(enemy_surface_mirrored, (enemy_x, enemy_y))
        enemy_x += 5
    elif keys[pygame.K_LEFT]:
        enemy_x -= 5
        screen.blit(enemy_surface, (enemy_x, enemy_y))
    else:
        screen.blit(enemy_surface, (enemy_x, enemy_y))

    # Clamp enemy inside screen
    enemy_x = max(0, min(enemy_x, screen.get_width() - enemy_surface.get_width() + 30))

    pygame.display.update()
    clock.tick(60)
