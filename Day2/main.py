"""Advent of Code 2025 - Day 1"""

INPUT_FILE = "/workspaces/AdventOfCode2025/Day2/input.txt"


def solve_part1() -> int:
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
                    snum = str(start)
                    if len(snum) % 2 == 1:
                        start += 1
                        continue
                    front = 0
                    end = int(len(snum) / 2)
                    while end < len(snum):
                        if snum[front] != snum[end]:
                            break
                        front += 1
                        end += 1
                        if end == len(snum):
                            result += start
                    start += 1

    return result


def is_num_valid(num) -> bool:
    snum = str(num)
    for i in range(1, 11):
        if len(snum) % i == 0:
            sequence = snum[:i]
            pos = i
            while pos + i <= len(snum):
                if sequence != snum[pos:pos+i]:
                    break
                if pos + i == len(snum):
                    return False
                pos += i
    return True

def solve_part2() -> int:
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
    print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))