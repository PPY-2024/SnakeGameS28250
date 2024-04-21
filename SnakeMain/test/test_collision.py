import pygame
import pytest

from src.game import Game
from src.point import Point


def test_instant_left_collision():
    game = Game(5, 5, "Test")
    game.snake.body[0] = Point(0, 0)
    game.snake.changeDirection(pygame.K_LEFT)
    game.snake.move()
    game.update()
    assert game.game_over is True


def test_self_collision():
    game = Game(10, 10, "Test")

    game.snake.body = [Point(120, 80), Point(140, 80), Point(140, 100), Point(120, 100), Point(100, 100)]
    game.snake.changeDirection(pygame.K_DOWN)
    game.snake.move()
    game.update()
    assert game.game_over is True


def test_no_collision():
    game = Game(10, 10, "Test")
    game.snake.body[0] = Point(100, 100)
    game.snake.move()
    game.update()
    assert game.game_over is False
