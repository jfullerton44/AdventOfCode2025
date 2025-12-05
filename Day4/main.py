"""Advent of Code 2025 - Day X"""

INPUT_FILE = "/workspaces/AdventOfCode2025/Day4/input.txt"

def is_valid(rows, i, j) -> bool:
    count = 0
    for k in range(i-1,i+2):
        for n in range(j-1,j+2):
            if k < 0 or k >= len(rows) or n < 0 or n >= len(rows[k]):
                continue
            if rows[k][n] == "@":
                count += 1
    return count <= 4

def solve_part1() -> int:
    result = 0

    with open(INPUT_FILE, "r") as file:
        rows = []
        for line in file:
            row = []
            line = line.strip()
            for letter in line:
                row.append(letter)
            rows.append(row)
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == "@":
                if is_valid(rows,i,j):
                    result+=1
                    # print(str(i) + " " + str(j))


    return result

def solve_part2() -> int:
    result = 0

    with open(INPUT_FILE, "r") as file:
        rows = []
        for line in file:
            row = []
            line = line.strip()
            for letter in line:
                row.append(letter)
            rows.append(row)
    curr = -1
    while curr != 0:
        curr = 0
        to_remove = []
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                if rows[i][j] == "@":
                    if is_valid(rows,i,j):
                        result+=1
                        curr += 1
                        to_remove.append((i,j))
        while len(to_remove) > 0:
            (i, j) = to_remove.pop()
            rows[i][j] = "."
    return result


if __name__ == "__main__":
    print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))