from day_3 import diagnostic_report_to_binary_numbers, nth_bits_of_each_number, most_common_bit, \
    compute_gamma_rate_in_binary, binary_to_decimal, least_common_bit, compute_epsilon_rate_in_binary, compute_power_consumption


def test_parsing_diagnostic_report():
    # Given
    diagnostic_report = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

    # When
    binary_numbers = list(diagnostic_report_to_binary_numbers(diagnostic_report))

    # Then
    assert binary_numbers == ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
                              "00010", "01010"]


def test_fetch_first_bits_of_each_number():
    # Given
    binary_numbers = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
                      "00010", "01010"]

    # When
    first_bits_of_each_number = list(nth_bits_of_each_number(binary_numbers, n=1))

    # Then
    assert len(first_bits_of_each_number) == len(binary_numbers)
    assert first_bits_of_each_number == [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0]


def test_fetch_second_bits_of_each_number():
    # Given
    binary_numbers = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
                      "00010", "01010"]

    # When
    second_bits_of_each_number = list(nth_bits_of_each_number(binary_numbers, n=2))

    # Then
    assert len(second_bits_of_each_number) == len(binary_numbers)
    assert second_bits_of_each_number == [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]


def test_most_common_bit():
    # Given
    first_bits_of_each_number = [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0]
    second_bits_of_each_number = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]

    # Then
    assert most_common_bit(first_bits_of_each_number) == 1
    assert most_common_bit(second_bits_of_each_number) == 0


def test_compute_gamma_rate_in_binary():
    # Given
    binary_numbers = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
                      "00010", "01010"]

    # Then
    assert compute_gamma_rate_in_binary(binary_numbers) == "10110"


def test_binary_to_decimal():
    # Given
    binary_number = "10110"
    another_binary_number = "01001"

    # When
    decimal_gamma_rate = binary_to_decimal(binary_number)
    decimal_epsilon_rate = binary_to_decimal(another_binary_number)

    # Then
    assert decimal_gamma_rate == 22
    assert decimal_epsilon_rate == 9


def test_least_common_bit():
    # Given
    first_bits_of_each_number = [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0]
    second_bits_of_each_number = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]

    # Then
    assert least_common_bit(first_bits_of_each_number) == 0
    assert least_common_bit(second_bits_of_each_number) == 1


def test_compute_epsilon_rate_in_binary():
    # Given
    binary_numbers = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
                      "00010", "01010"]

    # Then
    assert compute_epsilon_rate_in_binary(binary_numbers) == "01001"


def test_power_consumption():
    # Given
    gamma_rate, epsilon_rate = 22, 9

    # When
    p_consumption = compute_power_consumption(gamma_rate, epsilon_rate)

    # Then
    assert p_consumption == 198
