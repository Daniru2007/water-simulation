import pygame
import sys
from engine import Entity

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
        self.def_y = y
        self.time = 0

    def move(self, px, py):
        if abs(py - self.def_y) < 50 and abs(px - self.def_x) < 100:
            self.y += (py - self.y) / max(abs(px - self.x), 1)
            self.time += 1
        else:
            self.y += (self.def_y - self.y) / 20
            self.time = 0

    def display(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 1)


running = True
player = Entity(10, 10, 16, 16, "player")
player.load_animations("animations/player.json")
player.set_action("idle")
objects = []
for i in range(WINDOW_SIZE[0]):
    objects.append(Point(i, 200))
while running:
    player.gravity += 0.2
    if player.gravity > 2:
        player.gravity = 2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.gravity = -3
    screen.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()
    for object in objects:
        object.move(mx, my)
        object.display(screen)

    player.movement[1] += player.gravity
    player.move([])
    player.display(screen, [0, 0])
    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()
