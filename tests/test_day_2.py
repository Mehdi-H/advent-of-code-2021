from typing import List

from day_2 import Command, Direction, navigate_day_1, Position, product_of_final_position, string_to_direction, \
    string_to_command, navigate_day_2


def test_navigation():
    # Given
    commands: List[Command] = [Command(Direction.FORWARD, 5), Command(Direction.DOWN, 5),
                               Command(Direction.FORWARD, 8), Command(Direction.UP, 3),
                               Command(Direction.DOWN, 8), Command(Direction.FORWARD, 2)]

    # When
    position: Position = navigate_day_1(commands)

    # Then
    assert position == Position(15, 10, 0)


def test_product_of_final_position():
    # Given
    final_position: Position = Position(15, 10, 0)

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


# Day 2

def test_forward_5_goes_5_0_0():
    """forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change."""
    # Given
    commands: List[Command] = [Command(Direction.FORWARD, 5)]

    # When
    position: Position = navigate_day_2(commands)

    # Then
    assert position == Position(5, 0, 0)


def test_down_5_goes_5_0_5():
    """down 5 adds 5 to your aim, resulting in a value of 5."""
    # Given
    commands: List[Command] = [Command(Direction.FORWARD, 5), Command(Direction.DOWN, 5)]

    # When
    position: Position = navigate_day_2(commands)

    # Then
    assert position == Position(5, 0, 5)


def test_forward_8_goes_13_40_5():
    # Given
    commands: List[Command] = [Command(Direction.FORWARD, 5), Command(Direction.DOWN, 5), Command(Direction.FORWARD, 8)]

    # When
    position: Position = navigate_day_2(commands)

    # Then
    assert position == Position(13, 40, 5)


def test_up_3_goes_13_40_2():
    # Given
    commands: List[Command] = [Command(Direction.FORWARD, 5), Command(Direction.DOWN, 5),
                               Command(Direction.FORWARD, 8), Command(Direction.UP, 3)]

    # When
    position: Position = navigate_day_2(commands)

    # Then
    assert position == Position(13, 40, 2)


def test_down_8_goes_13_40_10():
    # Given
    commands: List[Command] = [Command(Direction.FORWARD, 5), Command(Direction.DOWN, 5),
                               Command(Direction.FORWARD, 8), Command(Direction.UP, 3),
                               Command(Direction.DOWN, 8)]

    # When
    position: Position = navigate_day_2(commands)

    # Then
    assert position == Position(13, 40, 10)


def test_forward_2_goes_15_60_10():
    # Given
    commands: List[Command] = [Command(Direction.FORWARD, 5), Command(Direction.DOWN, 5),
                               Command(Direction.FORWARD, 8), Command(Direction.UP, 3),
                               Command(Direction.DOWN, 8), Command(Direction.FORWARD, 2)]

    # When
    position: Position = navigate_day_2(commands)

    # Then
    assert position == Position(15, 60, 10)


def test_product_of_final_position_at_day_2():
    # Given
    final_position: Position = Position(15, 60, 10)

    # When
    product: int = product_of_final_position(final_position)

    # Then
    assert product == 900
