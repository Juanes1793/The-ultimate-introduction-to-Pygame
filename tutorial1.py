import pygame
from sys import exit


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True
start_time = 0 

ground_surface = pygame.image.load("graphics/ground.png").convert()
sky_surface = pygame.image.load("graphics/Sky.png").convert()

# text_surface = test_font.render("My First Game", False, (64, 64, 64))
# text_rect = text_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))


player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
                
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                        player_gravity = -20
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = pygame.time.get_ticks()
        
    if game_active:

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, "#c0e8ec", text_rect)
        # pygame.draw.rect(screen, "#c0e8ec", text_rect,10)
        # screen.blit(text_surface, text_rect)
        display_score()
        snail_rect.left -= 4
        if snail_rect.right <= -100:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #COLLISION
        if snail_rect.colliderect(player_rect):
            game_active = False
    
    else:
        screen.fill("black")






    pygame.display.update()
    clock.tick(60)

    #TODO voy en el minuto 1:48 https://www.youtube.com/watch?v=AY9MnQ4x3zk
    
