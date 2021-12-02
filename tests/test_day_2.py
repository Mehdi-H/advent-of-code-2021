from typing import List

from day_2 import Command, Direction, navigate, Position, product_of_final_position, string_to_direction, \
    string_to_command


def test_navigation():
    # Given
    commands: List[Command] = [(Direction.FORWARD, 5), (Direction.DOWN, 5), (Direction.FORWARD, 8), (Direction.UP, 3),
                               (Direction.DOWN, 8), (Direction.FORWARD, 2)]

    # When
    position: Position = navigate(commands)

    # Then
    assert position == (15, 10)


def test_product_of_final_position():
    # Given
    final_position: Position = (15, 10)

    # When
    product: int = product_of_final_position(final_position)

    # Then
    assert product == 150


def test_string_to_direction():
    # Given
    strings = ["forward", "up", "down"]

    # When
    commands: List[Direction] = list(map(lambda s: string_to_direction(s), strings))

    # Then
    assert commands == [Direction.FORWARD, Direction.UP, Direction.DOWN]


def test_strings_to_command():
    # Given
    s = "forward 18"

    # When
    command = string_to_command(s)

    # Then
    assert command == (Direction.FORWARD, 18)
