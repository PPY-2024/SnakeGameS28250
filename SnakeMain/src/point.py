import pygame


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x
                and self.y == other.y)

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, pygame.Rect(self.x, self.y, 20, 20))
