import pygame
from point import Point

class Snake:
    def __init__(self, start_point):
        self.body = [Point(start_point.x - i * 20, start_point.y) for i in range(3)]
        self.direction = pygame.K_RIGHT
        self.growing = False
        self.sprite_sheet = pygame.image.load("../images/snake-graphics.png")
        self.tile_size = 64
        self.scaled_size = 20

    def move(self):
        global new_head
        head = self.body[0]
        if self.direction == pygame.K_RIGHT:
            new_head = Point(head.x + self.scaled_size, head.y)
        elif self.direction == pygame.K_LEFT:
            new_head = Point(head.x - self.scaled_size, head.y)
        elif self.direction == pygame.K_UP:
            new_head = Point(head.x, head.y - self.scaled_size)
        elif self.direction == pygame.K_DOWN:
            new_head = Point(head.x, head.y + self.scaled_size)

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

    def draw_segment(self, surface, point, tx, ty):
        rect = pygame.Rect(tx * self.tile_size, ty * self.tile_size, self.tile_size, self.tile_size)
        segment_image = self.sprite_sheet.subsurface(rect)
        scaled_segment = pygame.transform.scale(segment_image, (self.scaled_size, self.scaled_size))
        surface.blit(scaled_segment, (point.x, point.y))

    def draw_fruit(self, surface, fruit):
            rect = pygame.Rect(0, 3 * self.tile_size, self.tile_size, self.tile_size)
            fruit_image = self.sprite_sheet.subsurface(rect)
            scaled_fruit = pygame.transform.scale(fruit_image, (self.scaled_size, self.scaled_size))
            surface.blit(scaled_fruit, (fruit.x, fruit.y))

    def draw(self, surface):
        for i, point in enumerate(self.body):
            if i == 0:
                next_point = self.body[i + 1]
                if point.y < next_point.y:
                    self.draw_segment(surface, point, 3, 0)
                elif point.x > next_point.x:
                    self.draw_segment(surface, point, 4, 0)
                elif point.y > next_point.y:
                    self.draw_segment(surface, point, 4, 1)
                elif point.x < next_point.x:
                    self.draw_segment(surface, point, 3, 1)
            elif i == len(self.body) - 1:
                prev_point = self.body[i - 1]
                if prev_point.y < point.y:
                    self.draw_segment(surface, point, 3, 2)
                elif prev_point.x > point.x:
                    self.draw_segment(surface, point, 4, 2)
                elif prev_point.y > point.y:
                    self.draw_segment(surface, point, 4, 3)
                elif prev_point.x < point.x:
                    self.draw_segment(surface, point, 3, 3)
            else:
                prev_point = self.body[i - 1]
                next_point = self.body[i + 1]
                if (prev_point.x < point.x < next_point.x) or (next_point.x < point.x < prev_point.x):
                    self.draw_segment(surface, point, 1, 0)
                elif (prev_point.x < point.x and next_point.y > point.y) or (
                        next_point.x < point.x and prev_point.y > point.y):
                    self.draw_segment(surface, point, 2, 0)
                elif (prev_point.y < point.y < next_point.y) or (next_point.y < point.y < prev_point.y):
                    self.draw_segment(surface, point, 2, 1)
                elif (prev_point.y < point.y and next_point.x < point.x) or (
                        next_point.y < point.y and prev_point.x < point.x):
                    self.draw_segment(surface, point, 2, 2)
                elif (prev_point.x > point.x and next_point.y < point.y) or (
                        next_point.x > point.x and prev_point.y < point.y):
                    self.draw_segment(surface, point, 0, 1)
                elif (prev_point.y > point.y and next_point.x > point.x) or (
                        next_point.y > point.y and prev_point.x > point.x):
                    self.draw_segment(surface, point, 0, 0)
