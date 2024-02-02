import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000 )- start_time
    score_surface = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)

    return current_time

def obstacle_movent(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            screen.blit(snail_surface, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []
    


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True
start_time = 0 
score = 0
ground_surface = pygame.image.load("graphics/ground.png").convert()
sky_surface = pygame.image.load("graphics/Sky.png").convert()

# text_surface = test_font.render("My First Game", False, (64, 64, 64))
# text_rect = text_surface.get_rect(center=(400, 50))

# Obstacles
snail_surface = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

obstacle_rect_list = []


player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

#Into screen
player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

#Adding a text for the game title
game_title = test_font.render("Pixel Runner", False, (111, 196, 169))
game_title_rect = game_title.get_rect(center=(400, 50))

#Adding a text for the game instructions
game_instructions = test_font.render("Press space to run", False, (111, 196, 169))
game_instructions_rect = game_instructions.get_rect(center=(400, 350))


#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)



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
                start_time = int(pygame.time.get_ticks() / 1000 )
        
        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(snail_surface.get_rect(midbottom=(randint(900, 1100), 300)))
  
        
    if game_active:

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, "#c0e8ec", text_rect)
        # pygame.draw.rect(screen, "#c0e8ec", text_rect,10)
        # screen.blit(text_surface, text_rect)
        score = display_score()

        # snail_rect.left -= 4
        # if snail_rect.right <= -100:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #Obstacles movement
        obstacle_rect_list = obstacle_movent(obstacle_rect_list)

        #COLLISION
        if snail_rect.colliderect(player_rect):
            game_active = False
    
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_title, game_title_rect)

        if score == 0: 
            screen.blit(game_instructions, game_instructions_rect)
        else:
            screen.blit(score_message, score_message_rect)


    pygame.display.update()
    clock.tick(60)

    #TODO voy en el minuto 2:35 https://www.youtube.com/watch?v=AY9MnQ4x3zk
    
