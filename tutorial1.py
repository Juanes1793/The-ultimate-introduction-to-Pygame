import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

ground_surface = pygame.image.load("graphics/ground.png").convert()
sky_surface = pygame.image.load("graphics/Sky.png").convert()
text_surface = test_font.render("My First Game", False, "Black")

snail_surface = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_x_position = 600

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_x_position -= 4
    if snail_x_position <= -100:
        snail_x_position = 800
    screen.blit(snail_surface, (snail_x_position, 250))
    screen.blit(player_surface, (80, 200))


    pygame.display.update()
    clock.tick(60)

    #TODO voy en el minuto 55:20 https://www.youtube.com/watch?v=AY9MnQ4x3zk
    