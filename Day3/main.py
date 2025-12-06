"""Advent of Code 2025 - Day 3."""

from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def solve_part1() -> int:
    """
    Solve Part 1: Find two-digit numbers from largest digits.

    For each line, find the largest digit and then the largest digit
    after it to form a two-digit number.

    Returns:
        Sum of all two-digit numbers formed.
    """
    result = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            largest_digit = 0
            largest_pos = 0

            # Find the largest digit and its position
            for i in range(len(line) - 1):
                if int(line[i]) > largest_digit:
                    largest_digit = int(line[i])
                    largest_pos = i

            # Find the largest digit after the first one
            second_digit = 0
            for i in range(largest_pos + 1, len(line)):
                if int(line[i]) > second_digit:
                    second_digit = int(line[i])

            result += largest_digit * 10 + second_digit

    return result


def solve_part2() -> int:
    """
    Solve Part 2: Build 12-digit numbers from largest available digits.

    For each line, greedily select the largest digit at each step
    while ensuring enough digits remain for the full number.

    Returns:
        Sum of all 12-digit numbers formed.
    """
    result = 0
    num_digits = 12

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            current_num = 0
            pos = -1

            for j in range(num_digits):
                largest_digit = 0
                remaining_digits = num_digits - 1 - j

                for i in range(pos + 1, len(line) - remaining_digits):
                    if int(line[i]) > largest_digit:
                        largest_digit = int(line[i])
                        pos = i

                current_num = current_num * 10 + largest_digit

            result += current_num

    return result


if __name__ == "__main__":
    print(f"Part 1: {solve_part1()}")
    print(f"Part 2: {solve_part2()}")