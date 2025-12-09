"""Advent of Code 2025 - Day 9"""

from pathlib import Path
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


INPUT_FILE = Path(__file__).parent / "input.txt"


def print_grid(grid: list[list[int]]) -> None:
    """Print a 2D list in a readable format."""
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print()


def size(pt1: Point, pt2: Point) -> int:
    return (abs(pt1.x - pt2.x) + 1) * (abs(pt1.y - pt2.y) + 1)

def solve_part1() -> int:
    result = 0

    with open(INPUT_FILE, "r") as file:
        points = []
        for line in file:
            line = line.strip()
            x, y = line.split(",")
            points.append(Point(int(x), int(y)))
        for i in range(len(points)):
            for j in range(len(points)):
                if i >= j:
                    continue
                result = max(result, size(points[i], points[j]))

    return result


def flood_fill(grid: list[list[int]]) -> None:
    queue: list[Point] = []
    queue.append(Point(0, 0))
    while len(queue) > 0:
        pt = queue.pop(0)
        grid[pt.y][pt.x] = 0
        if pt.y > 0 and grid[pt.y - 1][pt.x] == -1:
            grid[pt.y - 1][pt.x] = 0
            queue.append(Point(pt.x, pt.y - 1))
        if pt.x > 0 and grid[pt.y][pt.x - 1] == -1:
            grid[pt.y][pt.x - 1] = 0
            queue.append(Point(pt.x - 1, pt.y))
        if pt.x < len(grid[0]) - 1 and grid[pt.y][pt.x + 1] == -1:
            grid[pt.y][pt.x + 1] = 0
            queue.append(Point(pt.x + 1, pt.y))
        if pt.y < len(grid) - 1 and grid[pt.y + 1][pt.x] == -1:
            grid[pt.y + 1][pt.x] = 0
            queue.append(Point(pt.x, pt.y + 1))

def rect_prefix_area(prefix: list[list[int]], pt1: Point, pt2: Point) -> int:
    area = prefix[pt2.y][pt2.x]
    if pt1.x > 0:
        area -= prefix[pt2.y][pt1.x - 1]
    if pt1.y > 0:
        area -= prefix[pt1.y - 1][pt2.x]
    if pt1.x > 0 and pt1.y > 0:
        area += prefix[pt1.y - 1][pt1.x - 1]
    return area

def solve_part2() -> int:
    result = 0

    with open(INPUT_FILE, "r") as file:
        points = []
        x_max = 0
        y_max = 0
        x_values = []
        y_values = []
        for line in file:
            line = line.strip()
            x, y = line.split(",")
            pt = Point(int(x), int(y))
            x_values.append(pt.x)
            y_values.append(pt.y)
            points.append(pt)
        x_values = list(set(x_values))
        y_values = list(set(y_values))
        x_values.sort()
        y_values.sort()
        x_map = {}
        x_map_big_small = {}
        y_map = {}
        y_map_big_small = {}
        i = 1
        for val in x_values:
            x_map[i] = val
            x_map_big_small[val] = i
            i += 1
        j = 1
        for val in y_values:
            y_map[j] = val
            y_map_big_small[val] = j
            j += 1
        x_max = i + 1
        y_max = j + 1
        converted_pts = []
        for pt in points:
            converted_pts.append(Point(x_map_big_small[pt.x], y_map_big_small[pt.y]))
        grid = [[-1 for _ in range(x_max)] for _ in range(y_max)]
        
        for i in range(len(converted_pts)):
            pt = converted_pts[i]
            grid[pt.y][pt.x] = 1
            j = i + 1
            if j == len(converted_pts):
                j = 0
            nxt = converted_pts[j]
            if nxt.x == pt.x:
                for y in range(min(pt.y, nxt.y), max(pt.y, nxt.y) + 1):
                    grid[y][pt.x] = 1
            else:
                for x in range(min(pt.x, nxt.x), max(pt.x, nxt.x) + 1):
                    grid[pt.y][x] = 1
        flood_fill(grid)
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == -1:
                    grid[y][x] = 1
        prefix_grid = [[0 for _ in range(x_max)] for _ in range(y_max)]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                temp = grid[y][x]
                if x > 0:
                    temp += prefix_grid[y][x-1]
                if y > 0:
                    temp += prefix_grid[y-1][x]
                if x > 0 and y > 0:
                    temp -= prefix_grid[y-1][x-1]
                prefix_grid[y][x] = temp

        # print_grid(grid)
        # print()
        # print_grid(prefix_grid)
        # print(converted_pts)
        for i in range(len(converted_pts)):
            for j in range(len(converted_pts)):
                if i >= j:
                    continue
                pt1 = converted_pts[i]
                pt2 = converted_pts[j]
                # Ensure top-left and bottom-right corners
                top_left = Point(min(pt1.x, pt2.x), min(pt1.y, pt2.y))
                bottom_right = Point(max(pt1.x, pt2.x), max(pt1.y, pt2.y))
                prefix_area = rect_prefix_area(prefix_grid, top_left, bottom_right)
                rect_size = size(top_left, bottom_right)
                if prefix_area == rect_size:
                    cpt1 = Point(x_map[pt1.x], y_map[pt1.y])
                    cpt2 = Point(x_map[pt2.x], y_map[pt2.y])
                    result = max(result, size(cpt1, cpt2))
                
    return result


if __name__ == "__main__":
    print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))