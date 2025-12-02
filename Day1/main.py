"""Advent of Code 2025 - Day 1"""

INPUT_FILE = "input.txt"
TRACK_LENGTH = 100
STARTING_POSITION = 50


def parse_instruction(line: str) -> tuple[str, int]:
    """Parse a line into direction and value."""
    direction = line[0]
    value = int(line[1:])
    return direction, value


def normalize_position(position: int) -> int:
    """Wrap position to stay within track bounds [0, TRACK_LENGTH)."""
    return position % TRACK_LENGTH


def solve_part1() -> int:
    """Solve part 1: Move by full value, count crossings at position 0."""
    position = STARTING_POSITION
    result = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            direction, value = parse_instruction(line)
            print(f"Direction: {direction}, Value: {value}")

            if direction == "R":
                position += value
            elif direction == "L":
                position -= value

            position = normalize_position(position)

            if position == 0:
                result += 1

    return result


def solve_part2() -> int:
    """Solve part 2: Move step by step, count each crossing at position 0."""
    position = STARTING_POSITION
    result = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            direction, value = parse_instruction(line)

            for _ in range(value):
                if direction == "R":
                    position += 1
                elif direction == "L":
                    position -= 1

                position = normalize_position(position)

                if position == 0:
                    result += 1

    return result


if __name__ == "__main__":
    print(solve_part1())
    print(solve_part2())