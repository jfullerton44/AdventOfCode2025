"""Advent of Code 2025 - Day X"""

INPUT_FILE = "/workspaces/AdventOfCode2025/Day5/input.txt"


def solve_part1() -> int:
    result = 0

    with open(INPUT_FILE, "r") as file:
        build = True
        ranges = []
        for line in file:
            line = line.strip()
            if line == "" or line is None:
                build = False
                continue
            
            if build:
                split = line.split("-")
                range = [int(split[0]), int(split[1])]
                ranges.append(range)
            else:
                value = int(line)
                for range in ranges:
                    if value >= range[0] and value <= range[1]:
                        result += 1
                        break

    return result

def solve_part2() -> int:
    result = 0

    with open(INPUT_FILE, "r") as file:
        ranges = []
        for line in file:
            line = line.strip()
            if line == "" or line is None:
                build = False
                break
            
            split = line.split("-")
            rng = [int(split[0]), int(split[1])]
            insetPosition = -1
            removeAt = []
            for i in range(len(ranges)):
                if rng[0] < ranges[i][0] and rng[1] > ranges[i][1]:
                    if not i in removeAt:
                        removeAt.append(i)
                if rng[1] >= ranges[i][0] and rng[1] <= ranges[i][1]:
                    rng[1] = max(ranges[i][1], rng[1])
                    if not i in removeAt:
                        removeAt.append(i)
                if rng[0] <= ranges[i][1] and rng[0] >= ranges[i][0]:
                    rng[0] = min(ranges[i][0], rng[0])
                    if not i in removeAt:
                        removeAt.append(i)
                if rng[0] > ranges[i][1]:
                    insetPosition = i
            if len(removeAt) == 1:
                ranges[removeAt[0]] = rng
            elif len(removeAt) > 1:
                ranges[removeAt[0]] = rng
                removeAt.pop(0)
                for index in sorted(removeAt, reverse=True):
                    del ranges[index]
            else:
                ranges.insert(insetPosition+1, rng)
    
    for rng in ranges:
        result += rng[1] - rng[0] + 1
        print(rng)
    return result


if __name__ == "__main__":
    print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))