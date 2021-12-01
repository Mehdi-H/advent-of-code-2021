from typing import List


def number_times_depth_increases(depths: List[int]):
    return sum((1 if (pair[0] < pair[1]) else 0 for pair in (_list_to_pairs(depths))))


def _list_to_pairs(depths):
    for i in range(0, len(depths) - 1):
        yield tuple(depths[i:i + 2])


if __name__ == '__main__':
    with open('input.txt') as f:
        depths: List[int] = [int(n) for n in f.readlines()]
    print(number_times_depth_increases(depths))  # 1752
