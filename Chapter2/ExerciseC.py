import pygame

pygame.init()
screen_width = 800
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)

pygame.font.init()
font = pygame.font.Font('fonts/PrStart.ttf', 60)
subtitle_font = pygame.font.Font('fonts/Monocraft.ttf', 12)

text = font.render('Hadi Chaaban', False, white)
subtitle_text = font.render('Software Engineer', False, blue)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(text, (0, 0))
    screen.blit(subtitle_text, (0, text.get_height()))
    pygame.display.update()
pygame.quit()