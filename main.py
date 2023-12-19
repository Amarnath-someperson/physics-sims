import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1600, 900))
fps = 60
screen.fill((0,0,0))
pygame.display.set_caption('Physics Simulations')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # ends all code, safer than break

    pygame.display.update()
    pygame.time.Clock().tick(fps)
