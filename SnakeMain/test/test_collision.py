import pytest

from src.CustomDataStr import Point


def test_instant_left_collision():
    game = Game(5, 5)
    game.snake.head = Point(0, 0)
    game.snake.move('LEFT')
    game.update()
    assert game.game_over == True


def test_self_collision():
    game = Game(10, 10)
    game.snake.body = [Point(6, 6), Point(6, 7), Point(5, 7), Point(5, 6), Point(5, 5)]
    game.snake.move('UP')
    game.update()
    assert game.game_over == True


def test_no_collision():
    game = Game(10, 10)
    game.snake.head = Point(5, 5)
    game.snake.move('RIGHT')
    game.update()
    assert game.game_over == False
