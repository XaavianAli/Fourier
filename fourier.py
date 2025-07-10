import pygame
import math

WIDTH = 2
screen = None

class circle:
    origin = [0.0]
    radius = 1
    frequency = 1
    rotation_raw = 270
    rotation = -math.radians(rotation_raw%360)
    point = [0,0]
    surface = None
    color = 0x000000

    def __init__(self, origin, radius, frequency, surface, color):
        self.origin = origin
        self.radius = radius
        self.frequency = frequency
        self.surface = screen
        self.color = color
        self.point = [self.origin[0] + self.radius*math.cos(self.rotation), self.origin[1] + self.radius*math.sin(self.rotation)]

    def update(self):
        self.point = [self.origin[0] + self.radius*math.cos(self.rotation), self.origin[1] + self.radius*math.sin(self.rotation)]

    def draw(self):
        self.update()
        pygame.draw.circle(self.surface, self.color, self.origin, self.radius, WIDTH)
        pygame.draw.circle(self.surface, 0xff0000, self.point, 2, WIDTH)



pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True

circles = [
    circle([500,500], 50, 1, screen, 0x000000),
    #circle([500,500], 70, 1, screen, 0x000000)
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(0xffffff)

    # RENDER YOUR GAME HERE
    x = 0
    while (x < len(circles)):
        if x > 0:
            circles[x].origin = circles[x-1].point

        circles[x].draw()
        x = x + 1

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
