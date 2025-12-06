"""Advent of Code 2025 - Day 5."""

from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def solve_part1() -> int:
    """
    Solve Part 1: Count values that fall within defined ranges.

    The input file has two sections separated by a blank line:
    1. Range definitions (start-end format)
    2. Values to check against the ranges

    Returns:
        Count of values that fall within any of the defined ranges.
    """
    result = 0
    ranges: list[list[int]] = []
    building_ranges = True

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()

            if line == "" or line is None:
                building_ranges = False
                continue

            if building_ranges:
                parts = line.split("-")
                rng = [int(parts[0]), int(parts[1])]
                ranges.append(rng)
            else:
                value = int(line)
                for rng in ranges:
                    if rng[0] <= value <= rng[1]:
                        result += 1
                        break

    return result


def solve_part2() -> int:
    """
    Solve Part 2: Merge overlapping ranges and count total coverage.

    Reads range definitions and merges overlapping or adjacent ranges,
    then calculates the total number of values covered.

    Returns:
        Total count of values covered by all merged ranges.
    """
    result = 0
    ranges: list[list[int]] = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()

            if line == "" or line is None:
                break

            parts = line.split("-")
            new_range = [int(parts[0]), int(parts[1])]
            insert_position = -1
            indices_to_remove: list[int] = []

            # Check for overlaps with existing ranges
            for i in range(len(ranges)):
                # New range completely contains existing range
                if new_range[0] < ranges[i][0] and new_range[1] > ranges[i][1]:
                    if i not in indices_to_remove:
                        indices_to_remove.append(i)

                # New range end overlaps with existing range
                if ranges[i][0] <= new_range[1] <= ranges[i][1]:
                    new_range[1] = max(ranges[i][1], new_range[1])
                    if i not in indices_to_remove:
                        indices_to_remove.append(i)

                # New range start overlaps with existing range
                if ranges[i][0] <= new_range[0] <= ranges[i][1]:
                    new_range[0] = min(ranges[i][0], new_range[0])
                    if i not in indices_to_remove:
                        indices_to_remove.append(i)

                # Track insertion position for non-overlapping case
                if new_range[0] > ranges[i][1]:
                    insert_position = i

            # Merge or insert the new range
            if len(indices_to_remove) == 1:
                ranges[indices_to_remove[0]] = new_range
            elif len(indices_to_remove) > 1:
                ranges[indices_to_remove[0]] = new_range
                for index in sorted(indices_to_remove[1:], reverse=True):
                    del ranges[index]
            else:
                ranges.insert(insert_position + 1, new_range)

    # Calculate total coverage
    for rng in ranges:
        result += rng[1] - rng[0] + 1

    return result


if __name__ == "__main__":
    print(f"Part 1: {solve_part1()}")
    print(f"Part 2: {solve_part2()}")