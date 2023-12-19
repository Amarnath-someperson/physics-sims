import pygame
from sys import exit

pygame.init()
pygame.display.set_caption('Physics Simulations')

screen = pygame.display.set_mode((1600, 900))
screen.fill((0,0,0))
width = screen.get_width()
height = screen.get_height()
fps = 60
WHITE = (255, 255, 255)
font = pygame.font.SysFont('Arial', 24)
text = font.render('Particle Collider' , False , WHITE) 
box = text.get_width()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # ends all code, safer than break
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            
            
    mouse = pygame.mouse.get_pos()
    screen.blit(text, (width//2-box//2, height//2))        
    
    pygame.display.update()
    pygame.time.Clock().tick(fps)
