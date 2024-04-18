import pytest

from src.CustomDataStr import Point


def test_correct_increasing():
    game = Game(25, 25)
    game.snake.head = Point(5, 5)
    game.apple = Point(5, 6)
    game.snake.move('RIGHT')
    game.update()
    assert game.score == 4  # initial size is always 3

def test_no_increasing():
    game = Game(25, 25)
    game.snake.head = Point(5, 5)
    game.apple = Point(10, 5)
    game.snake.move('RIGHT')
    game.update()
    assert game.score == 3