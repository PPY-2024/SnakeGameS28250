import pygame

from point import Point


class Snake:

    def __init__(self, start_point):
        self.body = [Point(start_point.x - i * 20, start_point.y) for i in range(3)]
        self.direction = pygame.K_RIGHT
        self.growing = False

    def move(self):
        global new_head
        head = self.body[0]
        if self.direction == pygame.K_RIGHT:
            new_head = Point(head.x + 20, head.y)
        elif self.direction == pygame.K_LEFT:
            new_head = Point(head.x - 20, head.y)
        elif self.direction == pygame.K_UP:
            new_head = Point(head.x, head.y - 20)
        elif self.direction == pygame.K_DOWN:
            new_head = Point(head.x, head.y + 20)

        if self.growing:
            self.body.insert(0, new_head)
            self.growing = False
        else:
            self.body.insert(0, new_head)
            self.body.pop()

    def changeDirection(self, key):
        self.direction = key

    def grow(self):
        self.growing = True

    def draw(self, surface, color):
        for point in self.body:
            point.draw(surface, color)
