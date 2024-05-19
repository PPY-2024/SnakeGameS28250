import random
import pygame
from point import Point
from snake import Snake
from src.mongoDB import store_game_result, dump_data_to_file


class Game:
    def __init__(self, widthSquares, heightSquares, text):
        pygame.init()

        self.widthPixels = widthSquares * 20
        self.heightPixels = heightSquares * 20
        self.snake = Snake(Point((widthSquares // 2) * 20, (heightSquares // 2) * 20))
        self.fruit = None
        self.score = 3
        self.game_over = False
        self.generate_fruit()
        self.screen = pygame.display.set_mode((self.widthPixels, self.heightPixels))
        pygame.display.set_caption(text)

    def generate_fruit(self):
        while True:
            x = random.randint(0, (self.widthPixels // 20) - 1) * 20
            y = random.randint(0, (self.heightPixels // 20) - 1) * 20
            self.fruit = Point(x, y)
            if self.fruit not in self.snake.body:
                break

    def update(self):
        if self.snake.body[0] == self.fruit:
            self.snake.grow()
            self.score += 1
            self.generate_fruit()
        if (self.snake.body[0].x < 0 or self.snake.body[0].x >= self.widthPixels or
                self.snake.body[0].y < 0 or self.snake.body[0].y >= self.heightPixels or
                self.snake.body[0] in self.snake.body[1:]):
            self.game_over = True
            store_game_result("PlayerName", f"{self.widthPixels}x{self.heightPixels}", self.score)

    def run(self):
        clock = pygame.time.Clock()
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.snake.changeDirection(event.key)
            if not self.game_over:
                self.snake.move()
                self.update()

            self.screen.fill((237, 244, 242))

            for x in range(0, self.widthPixels, 20):
                for y in range(0, self.heightPixels, 20):
                    pygame.draw.rect(self.screen, (200, 200, 200), pygame.Rect(x, y, 20, 20), 1)

            self.snake.draw(self.screen, (49, 71, 58))
            self.fruit.draw(self.screen, (255, 0, 0))
            pygame.display.flip()
            clock.tick(10)

        dump_data_to_file("db/data.json")
        print("Game over | score: ", self.score)
