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

font = pygame.font.SysFont('Corbel', 24)
head = pygame.font.SysFont('Corbel', 60).render('Menu', False, WHITE)
text = font.render('Particle Collider' , False , WHITE) 
box = text.get_size()

select=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # ends all code, safer than break
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse:
                select = True
                pass
            
            
    mouse = pygame.mouse.get_pos()
    if select:
        screen.fill((20, 80, 170))
    if not select:
        screen.blit(head, (width//2-head.get_width()//2, height//2-head.get_height()//2-100))
        screen.blit(text, (width//2-box[0]//2, height//2-box[1]//2))        
    pygame.display.update()
    pygame.time.Clock().tick(fps)
