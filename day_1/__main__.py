from typing import List, Tuple


def number_times_depth_increases(depths: List[int], measurement_sliding_window: int = 1):
    groups_of_measurements: List[Tuple[int]] = group_measurements(depths, measurement_sliding_window)
    sums_by_group: List[int] = sum_groups_of_measurements(groups_of_measurements)
    tuples_of_depths = _list_to_tuples_of_depths(sums_by_group)
    return sum((1 if (pair[0] < pair[1]) else 0 for pair in tuples_of_depths))


def _list_to_tuples_of_depths(depths: List[int]):
    for i in range(0, len(depths) - 1):
        yield tuple(depths[i:i + 2])


def group_measurements(depths: List[int], measurement_sliding_window: int) -> List[Tuple[int]]:
    for i in range(0, len(depths) - measurement_sliding_window + 1):
        yield tuple(depths[i:i + measurement_sliding_window])


def sum_groups_of_measurements(groups) -> List[int]:
    return [sum(group) for group in groups]


if __name__ == '__main__':
    with open('input.txt') as f:
        depths: List[int] = [int(n) for n in f.readlines()]
    print(number_times_depth_increases(depths))  # 1752
    print(number_times_depth_increases(depths, measurement_sliding_window=3))  # 1781
