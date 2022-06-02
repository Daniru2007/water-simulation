import pygame
import sys
pygame.init()

WINDOW_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('water simulation')

clock = pygame.time.Clock()


class Point(object):
    def __init__(self, x, y):
        self.def_x = x
        self.x = x
        self.y = y

    def move(self, px, py):
        if abs(py - self.y) < 100 and abs(px - self.x) < 100:
            self.y += (py - self.y) / 10

    def display(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 1)


running = True
objects = []
for i in range(WINDOW_SIZE[0]):
    objects.append(Point(i, 100))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()
    for object in objects:
        object.move(mx, my)
        object.display(screen)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()
