from day_1 import number_times_depth_increases, group_measurements, sum_groups_of_measurements


def test_no_increase():
    # Given
    depths = [199, 199]

    # When
    increases = number_times_depth_increases(depths)

    # Then
    assert increases == 0


def test_one_increase():
    # Given
    depths = [199, 200]

    # When
    increases = number_times_depth_increases(depths)

    # Then
    assert increases == 1


def test_seven_increases():
    # Given
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    # When
    increases = number_times_depth_increases(depths)

    # Then
    assert increases == 7


# Part 2

def test_group_measurements_with_sliding_window_of_3():
    # Given
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    # When
    groups = group_measurements(depths, 3)

    # Then
    assert list(groups) == [
        (199, 200, 208), (200, 208, 210), (208, 210, 200),
        (210, 200, 207), (200, 207, 240), (207, 240, 269),
        (240, 269, 260), (269, 260, 263)
    ]


def test_sum_of_groups_of_measurements():
    # Given
    groups = [
        (199, 200, 208), (200, 208, 210), (208, 210, 200),
        (210, 200, 207), (200, 207, 240), (207, 240, 269),
        (240, 269, 260), (269, 260, 263)
    ]

    # When
    sums = sum_groups_of_measurements(groups)

    # Then
    assert sums == [607, 618, 618, 617, 647, 716, 769, 792]


def test_depths_increase_on_day_2():
    # Given
    depths = [607, 618, 618, 617, 647, 716, 769, 792]

    # When
    increases = number_times_depth_increases(depths)

    # Then
    assert increases == 5
