from typing import List


def diagnostic_report_to_binary_numbers(diagnostic_report: str) -> List[str]:
    yield from [number.strip() for number in diagnostic_report.split('\n')]


def nth_bits_of_each_number(binary_numbers: List[str], n: int) -> List[int]:
    return [int(number[n - 1]) for number in binary_numbers]


def most_common_bit(bits: List[int]) -> int:
    return max(set(bits), key=bits.count)


def least_common_bit(bits: List[int]) -> int:
    return min(set(bits), key=bits.count)


def compute_gamma_rate_in_binary(binary_numbers: List[str]) -> str:
    len_of_a_binary_number = len(binary_numbers[0])
    gamma_rate_bits = []
    for n in range(1, len_of_a_binary_number + 1):
        nth_bits = nth_bits_of_each_number(binary_numbers, n=n)
        gamma_rate_bits.append(str(most_common_bit(nth_bits)))
    return "".join(gamma_rate_bits)


def compute_epsilon_rate_in_binary(binary_numbers: List[str]) -> str:
    len_of_a_binary_number = len(binary_numbers[0])
    gamma_rate_bits = []
    for n in range(1, len_of_a_binary_number + 1):
        nth_bits = nth_bits_of_each_number(binary_numbers, n=n)
        gamma_rate_bits.append(str(least_common_bit(nth_bits)))
    return "".join(gamma_rate_bits)


def binary_to_decimal(binary_number: str) -> int:
    return int(binary_number, 2)


def compute_power_consumption(gamma_rate: int, epsilon_rate: int) -> int:
    return gamma_rate * epsilon_rate


if __name__ == '__main__':
    with open('input_day_3.txt', 'r') as f:
        binary_numbers = [number.strip() for number in f.readlines()]
    gamma_rate = binary_to_decimal(compute_gamma_rate_in_binary(binary_numbers))
    epsilon_rate = binary_to_decimal(compute_epsilon_rate_in_binary(binary_numbers))
    power_consumption = compute_power_consumption(gamma_rate, epsilon_rate)
    print(power_consumption)  # 3309596
