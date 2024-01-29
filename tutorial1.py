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
text_rect = text_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))


player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, text_rect)
    snail_rect.left -= 4
    if snail_rect.right <= -100:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)




    pygame.display.update()
    clock.tick(60)

    #TODO voy en el minuto 55:20 https://www.youtube.com/watch?v=AY9MnQ4x3zk
    