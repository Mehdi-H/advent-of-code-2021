from dataclasses import dataclass
from enum import Enum, auto
from typing import List


class Direction(Enum):
    FORWARD = auto()
    DOWN = auto()
    UP = auto()


@dataclass
class Command:
    direction: Direction
    units: int


@dataclass
class Position:
    horizontal_position: int
    depth: int
    aim: int


def update_position_day_1(current_position: Position,
                          horizontal_movement: int, vertical_movement: int, aim_amount: int = 0) -> Position:
    new_horizontal_position: int = current_position.horizontal_position + horizontal_movement
    new_depth: int = current_position.depth + vertical_movement
    return Position(new_horizontal_position, new_depth, aim_amount)


def update_position_day_2(current_position: Position,
                          horizontal_movement: int, aim_amount: int = 0) -> Position:
    going_forward = (horizontal_movement != 0)
    if going_forward:
        new_horizontal_position: int = current_position.horizontal_position + horizontal_movement
        new_depth: int = current_position.depth + (current_position.aim * horizontal_movement)
        new_aim: int = current_position.aim
    else:
        new_horizontal_position: int = current_position.horizontal_position
        new_depth: int = current_position.depth
        new_aim: int = current_position.aim + aim_amount
    return Position(new_horizontal_position, new_depth, new_aim)


def navigate_day_1(commands: List[Command]) -> Position:
    current_position: Position = Position(0, 0, 0)
    for command in commands:
        match command.direction:
            case Direction.FORWARD:
                current_position = update_position_day_1(
                    current_position, horizontal_movement=command.units, vertical_movement=0)
            case Direction.UP:
                current_position = update_position_day_1(
                    current_position, horizontal_movement=0, vertical_movement=command.units * -1)
            case Direction.DOWN:
                current_position = update_position_day_1(
                    current_position, horizontal_movement=0, vertical_movement=command.units)
    return current_position


def navigate_day_2(commands: List[Command]) -> Position:
    current_position = Position(0, 0, 0)
    for command in commands:
        match command.direction:
            case Direction.FORWARD:
                current_position = update_position_day_2(
                    current_position,
                    horizontal_movement=command.units,
                    aim_amount=current_position.aim)
            case Direction.UP:
                current_position = update_position_day_2(
                    current_position, horizontal_movement=0, aim_amount=command.units * -1)
            case Direction.DOWN:
                current_position = update_position_day_2(
                    current_position, horizontal_movement=0, aim_amount=command.units)
    return current_position


def product_of_final_position(position: Position) -> int:
    return position.horizontal_position * position.depth


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
    return Command(direction=string_to_direction(string_to_list[0]), units=int(string_to_list[1]))


if __name__ == '__main__':
    with open('input_day_2.txt') as f:
        commands: List[Command] = [string_to_command(s) for s in f.readlines()]
    print(product_of_final_position(navigate_day_1(commands)))  # 1813801
    print(product_of_final_position(navigate_day_2(commands)))  # 1960569556
