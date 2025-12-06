"""Advent of Code 2025 - Day 6."""

from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def solve_part1() -> int:
    """
    Solve Part 1: Process columns with arithmetic operations.

    Reads numbers into columns, then applies + or * operations
    to each column when an operation row is encountered.

    Returns:
        Sum of all operation results.
    """
    result = 0
    columns: list[list[int]] = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            tokens = line.split(" ")
            col_idx = 0

            # Check if this is an operation row
            if tokens[0] in ("+", "*"):
                for op in tokens:
                    if op.strip() == "":
                        continue

                    if op == "+":
                        result += sum(columns[col_idx])
                    elif op == "*":
                        product = 1
                        for val in columns[col_idx]:
                            product *= val
                        result += product

                    col_idx += 1
                continue

            # Parse number row into columns
            for num in tokens:
                if num.strip() == "":
                    continue

                while len(columns) <= col_idx:
                    columns.append([])

                columns[col_idx].append(int(num))
                col_idx += 1

    return result


def solve_part2() -> int:
    """
    Solve Part 2: Process digit columns with grouped operations.

    Builds numbers from individual digits in columns, then applies
    operations based on groupings in the operation row.

    Returns:
        Sum of all grouped operation results.
    """
    result = 0
    columns: list[int] = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            tokens = line.split(" ")

            # Check if this is an operation row
            if tokens[0] in ("+", "*"):
                i = 0
                while i < len(line):
                    op = line[i]
                    temp = columns[i]
                    i += 1

                    # Group consecutive empty positions with same operation
                    while i < len(line) and line[i].strip() == "":
                        if i == len(line) - 1 or line[i + 1].strip() == "":
                            if op == "*":
                                temp *= columns[i]
                            else:
                                temp += columns[i]
                        i += 1

                    result += temp

                return result

            # Build numbers from digits in each column
            for i in range(len(line)):
                if line[i].strip() == "":
                    continue

                while len(columns) <= i:
                    columns.append(0)

                columns[i] = columns[i] * 10 + int(line[i])

    return result


if __name__ == "__main__":
    print(f"Part 1: {solve_part1()}")
    print(f"Part 2: {solve_part2()}")