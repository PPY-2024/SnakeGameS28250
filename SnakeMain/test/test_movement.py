import pygame
import pytest

from src.point import Point
from src.snake import Snake


def test_correct_initial_position():
    snake = Snake(Point(100, 100))
    assert snake.body[0] == Point(100, 100)


def test_incorrect_initial_position():
    snake = Snake(Point(100, 100))
    assert snake.body[0] != Point(60, 60)


def test_snake_move_right():
    snake = Snake(Point(100, 100))
    snake.move()
    assert snake.body[0] == Point(120, 100)


def test_snake_move_left():
    snake = Snake(Point(100, 100))
    snake.changeDirection(pygame.K_LEFT)
    snake.move()
    assert snake.body[0] == Point(80, 100)


def test_snake_move_up():
    snake = Snake(Point(100, 100))
    snake.changeDirection(pygame.K_UP)
    snake.move()
    assert snake.body[0] == Point(100, 80)


def test_snake_move_down():
    snake = Snake(Point(100, 100))
    snake.changeDirection(pygame.K_DOWN)
    snake.move()
    assert snake.body[0] == Point(100, 120)
