"""Advent of Code 2025 - Day 1"""

INPUT_FILE = "/workspaces/AdventOfCode2025/Day3/input.txt"


def solve_part1() -> int:
    result = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            largestNum = 0
            pos = 0
            for i in range(len(line) - 1):
                if int(line[i]) > largestNum:
                    largestNum = int(line[i])
                    pos = i
            
            secondDigit = 0
            for i in range(pos+1, len(line)):
                if (int(line[i])) > secondDigit:
                    secondDigit = int(line[i])
            result += largestNum * 10 + secondDigit

    return result

def solve_part2() -> int:
    result = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            curr = 0
            largestNum = 0
            pos = -1
            for j in range(12):
                largestNum = 0
                for i in range(pos + 1, len(line) - (11-j)):
                    if int(line[i]) > largestNum:
                        largestNum = int(line[i])
                        pos = i
                curr *= 10
                curr += largestNum
            result += curr

    return result


if __name__ == "__main__":
    print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))