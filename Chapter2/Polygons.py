import numpy as np
import pygame
from pygame.locals import *

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False

def polygon_maker(array_of_points):
    color = list(np.random.choice(range(256), size=3))
    if len(array_of_points) > 2:
        pygame.draw.polygon(screen, color, array_of_points)
        return True
    if len(array_of_points) == 2:
        pygame.draw.line(screen, color, array_of_points[0], array_of_points[1], 1)
        return True
    return False
points = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            points.append(pygame.mouse.get_pos())
        elif event.type == KEYDOWN:
            polygon_maker(points)
            points = []
    pygame.display.update()
pygame.quit()