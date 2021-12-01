from day_1.__main__ import number_times_depth_increases


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
