import pytest

from src.CustomDataStr import Point


def test_correct_initial_position():
    snake = Snake()
    assert snake.head == Point(5, 5)


def test_incorrect_initial_position():
    snake = Snake()
    assert snake.head == Point(3, 3)


def test_snake_move_right():
    snake = Snake()
    initial_head = snake.head
    snake.move('RIGHT')
    assert snake.head == Point(initial_head.y, initial_head.x + 1)


def test_snake_move_left():
    snake = Snake()
    initial_head = snake.head
    snake.move('LEFT')
    assert snake.head == Point(initial_head.y, initial_head.x - 1)


def test_snake_move_up():
    snake = Snake()
    initial_head = snake.head
    snake.move('UP')
    assert snake.head == Point(initial_head.y + 1, initial_head.x)


def test_snake_move_down():
    snake = Snake()
    initial_head = snake.head
    snake.move('DOWN')
    assert snake.head == Point(initial_head.y - 1, initial_head.x)
