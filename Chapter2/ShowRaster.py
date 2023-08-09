import pygame
pygame.init()
screen_width = 190
screen_height = 266
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Starry Goku")
done = False
background = pygame.image.load('images/starrygoku.jpeg')
sprite = pygame.image.load('images/diamondhelmet.png')

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))
    screen.blit(sprite, (100, 100))
    pygame.display.update()
pygame.quit()