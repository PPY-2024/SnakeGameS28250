import pytest

from src.game import Game
from src.point import Point


def test_correct_increasing():
    game = Game(20, 20, "Test")
    game.fruit = Point(220, 200)
    game.snake.move()
    game.update()
    assert game.score == 4


def test_no_increasing():
    game = Game(25, 25, "Test")
    initial_length = len(game.snake.body)
    game.fruit = Point(200, 200)
    game.snake.move()
    game.update()
    assert game.score == initial_length
