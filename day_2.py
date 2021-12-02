from enum import Enum, auto
from functools import reduce
from typing import Tuple, List


class Direction(Enum):
    FORWARD = auto()
    DOWN = auto()
    UP = auto()


Units = int
Command = Tuple[Direction, Units]
Position = Tuple[Units, Units]


def update_position(current_position: Position, horizontal_movement: int, vertical_movement: int) -> Position:
    return current_position[0] + horizontal_movement, current_position[1] + vertical_movement


def navigate(commands: List[Command]) -> Position:
    current_position: Position = (0, 0)
    for command in commands:
        match command[0]:
            case Direction.FORWARD:
                current_position = update_position(
                    current_position, horizontal_movement=command[1], vertical_movement=0)
            case Direction.UP:
                current_position = update_position(
                    current_position, horizontal_movement=0, vertical_movement=command[1] * -1)
            case Direction.DOWN:
                current_position = update_position(
                    current_position, horizontal_movement=0, vertical_movement=command[1])
    return current_position


def product_of_final_position(position: Position) -> int:
    return reduce(lambda x, y: x * y, position)


def string_to_direction(s):
    match s:
        case "forward":
            return Direction.FORWARD
        case "down":
            return Direction.DOWN
        case "up":
            return Direction.UP
        case _:
            raise TypeError(f"direction {s} is not supported.")


def string_to_command(s):
    string_to_list = s.split(" ")
    return string_to_direction(string_to_list[0]), int(string_to_list[1])


if __name__ == '__main__':
    with open('input_day_2.txt') as f:
        commands: List[Command] = [string_to_command(s) for s in f.readlines()]
    print(product_of_final_position(navigate(commands)))  # 1813801
