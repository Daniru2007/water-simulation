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

    def move(self, px, py, gravity):
        if abs(gravity) > 1:
            if gravity > 0:
                if py > self.def_y:
                    if abs(py - self.def_y) < 50 and abs(px - self.def_x) < 100:
                        self.y += ((py - self.y) + gravity) / max(abs(px - self.x), 1)
                        return
            else:
                if py < self.def_y:
                    if abs(py - self.def_y) < 50 and abs(px - self.def_x) < 100:
                        self.y += ((py - self.y) + gravity) / max(abs(px - self.x), 1)
                        return

        self.y += (self.def_y - self.y) / 20

    def display(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 1)


running = True
player = Entity(10, 10, 16, 16, "player")
player.load_animations("animations/player.json")
player.set_action("idle")
tiles = []
for i in range(30):
    tiles.append(["1", pygame.Rect(i * 16, 250, 16, 16)])
objects = []
for i in range(WINDOW_SIZE[0]):
    objects.append(Point(i, 200))
while running:
    if player.y < 210:
        player.gravity += 0.2
        if player.gravity > 2:
            player.gravity = 2
    else:
        player.gravity += 0.2
        if player.gravity > 1:
            player.gravity = 1

    player.air_time += 1
    player.movement = [0,0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player.air_time < 6:
                    player.gravity = -6
            if event.key == pygame.K_RIGHT:
                player.right = True
            if event.key == pygame.K_LEFT:
                player.left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.right = False
            if event.key == pygame.K_LEFT:
                player.left = False
    player.movement[1] = player.gravity
    screen.fill((0, 0, 0))
    if player.right:
        player.movement[0] = 3
    if player.left:
        player.movement[0] = -3
    for tile in tiles:
        screen.blit(pygame.image.load("imgs/ground.png"), tile[1])
    for object in objects:
        object.move(player.x+8, player.y+8, player.gravity)
        object.display(screen)

    collisions = player.move(tiles)
    if collisions["bottom"]:
        player.gravity = 0
        player.air_time = 0
    player.display(screen, [0, 0])
    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()
