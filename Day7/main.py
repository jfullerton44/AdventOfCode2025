"""Advent of Code 2025 - Day X"""

from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"

def solve_part1() -> int:
    result = 0
    current = set()
    next = set()
    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            for i in range(len(line)):
                if line[i] == "S":
                    current.add(i)
                    break
                if line[i] == "^" and i in current:
                    next.add(i + 1)
                    next.add(i - 1)
                    result += 1
                    current.remove(i)
            for item in current:
                next.add(item)
            current = next
            next = set()
    return result

def solve_part2() -> int:
    result = 0
    current = {}
    next = {}
    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            for i in range(len(line)):
                if line[i] == "S":
                    current[i] = 1
                    break
                if line[i] == "^" and i in current:
                    if i + 1 in next:
                        next[i + 1] = next[i + 1] + current[i]
                    else:
                        next[i + 1] = current[i]
                    if i - 1 in next:
                        next[i - 1] = next[i - 1] + current[i]
                    else:
                        next[i - 1] = current[i]
                    current.pop(i)
            for key, value in current.items():
                if key in next:
                    next[key] += value
                else:
                    next[key] = value
            current = next
            next = {}
    for key, value in current.items():
        result += value
    return result


if __name__ == "__main__":
    print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))