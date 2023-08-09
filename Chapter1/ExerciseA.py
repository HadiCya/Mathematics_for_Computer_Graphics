import pygame
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)

def draw_star(x, y, size):
    pygame.draw.rect(screen, white, (x, y, size, size))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    draw_star(200, 600, 10)
    draw_star(400, 620, 10)
    draw_star(400, 400, 7)
    draw_star(700, 450, 30)
    draw_star(720, 300, 7)
    draw_star(900, 260, 7)
    draw_star(850, 200, 7)
    draw_star(750, 500, 7)
    draw_star(750, 750, 20)
    pygame.display.update()
pygame.quit()