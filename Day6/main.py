"""Advent of Code 2025 - Day X"""

INPUT_FILE = "/workspaces/AdventOfCode2025/Day6/input.txt"


def solve_part2() -> int:
    result = 0
    cols = []
    with open(INPUT_FILE, "r") as file:
        for line in file:
            nums = line.split(" ")
            if nums[0] == "+" or nums[0] == "*":
                i = 0
                while i < len(line):
                    op = line[i]
                    temp = cols[i]
                    i += 1
                    while i < len(line) and line[i].strip() == '' and (i == len(line) - 1 or line[i+1].strip() == ''):
                        if op == "*":
                            temp *= cols[i]
                        else:
                            temp += cols[i]
                        i += 1
                    result += temp
                    
                return result
            for i in range(len(line)):
                if line[i].strip() == '':
                    continue
                while len(cols) <= i:
                    cols.append(0)
                cols[i] = cols[i] * 10 + int(line[i])
        print(cols)
    return result

def solve_part1() -> int:
    result = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()

    return result


if __name__ == "__main__":
    print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))