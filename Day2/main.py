"""Advent of Code 2025 - Day 2."""

from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def solve_part1() -> int:
    """
    Solve Part 1: Find numbers with mirrored halves.

    Returns:
        Sum of all valid numbers in the given ranges.
    """
    result = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            parts = line.split(",")

            for part in parts:
                nums = part.split("-")
                start = int(nums[0])
                stop = int(nums[1])

                while start <= stop:
                    num_str = str(start)

                    # Skip odd-length numbers
                    if len(num_str) % 2 == 1:
                        start += 1
                        continue

                    # Check if front half mirrors back half
                    half_len = len(num_str) // 2
                    front_idx = 0
                    back_idx = half_len

                    while back_idx < len(num_str):
                        if num_str[front_idx] != num_str[back_idx]:
                            break
                        front_idx += 1
                        back_idx += 1

                        if back_idx == len(num_str):
                            result += start

                    start += 1

    return result


def is_num_valid(num: int) -> bool:
    """
    Check if a number contains a repeating sequence pattern.

    Args:
        num: The number to validate.

    Returns:
        True if the number does NOT have a repeating sequence pattern.
    """
    num_str = str(num)

    for seq_len in range(1, 11):
        if len(num_str) % seq_len == 0:
            sequence = num_str[:seq_len]
            pos = seq_len

            while pos + seq_len <= len(num_str):
                if sequence != num_str[pos : pos + seq_len]:
                    break
                if pos + seq_len == len(num_str):
                    return False
                pos += seq_len

    return True


def solve_part2() -> int:
    """
    Solve Part 2: Find numbers with repeating sequence patterns.

    Returns:
        Sum of all numbers that have repeating patterns.
    """
    result = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            parts = line.split(",")

            for part in parts:
                nums = part.split("-")
                start = int(nums[0])
                stop = int(nums[1])

                while start <= stop:
                    if not is_num_valid(start):
                        result += start
                    start += 1

    return result


if __name__ == "__main__":
    print(f"Part 1: {solve_part1()}")
    print(f"Part 2: {solve_part2()}")