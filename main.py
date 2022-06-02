import pygame
import sys
pygame.init()

WINDOW_SIZE = (600, 400)
gameDisplay = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('water simulation')

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()
