"""Advent of Code 2025 - Day X"""

from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def print_grid(grid):
    """Print a 2D list in a readable format."""
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print()


def size(pt1, pt2):
    return (abs(pt1[0]- pt2[0])+1) * (abs(pt1[1] - pt2[1]) + 1)

def solve_part1() -> int:
    result = 0

    with open(INPUT_FILE, "r") as file:
        points = []
        for line in file:
            line = line.strip()
            pt = line.split(",")
            for i in range(len(pt)):
                pt[i] = int(pt[i])
            points.append(pt)
        for i in range(len(points)):
            for j in range(len(points)):
                if i >= j:
                    continue
                result = max(result, size(points[i], points[j]))

    return result


def flood_fill(grid):
    queue = []
    queue.append([0,0])
    while len(queue) > 0:
        item = queue.pop(0)
        x, y = item[0], item[1]
        grid[y][x] = 0
        if y > 0 and grid[y - 1][x] == -1:
            grid[y - 1][x] = 0
            queue.append([x, y - 1])
        if x > 0 and grid[y][x - 1] == -1:
            grid[y][x - 1] = 0
            queue.append([x - 1, y])
        if x < len(grid[0]) - 1 and grid[y][x + 1] == -1:
            grid[y][x + 1] = 0
            queue.append([x + 1, y])
        if y < len(grid) - 1 and grid[y + 1][x] == -1:
            grid[y + 1][x] = 0
            queue.append([x, y + 1])

def rect_prefix_area(prefix, pt1, pt2):
    area = prefix[pt2[1]][pt2[0]]
    if pt1[0] > 0:
        area -= prefix[pt2[1]][pt1[0]-1]
    if pt1[1] > 0:
        area -= prefix[pt1[1] - 1][pt2[0]]
    if pt1[0] > 0 and pt1[1] > 0:
        area += prefix[pt1[1]-1][pt1[0]-1]
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
            pt = line.split(",")
            for i in range(len(pt)):
                pt[i] = int(pt[i])
            x_values.append(pt[0])
            y_values.append(pt[1])
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
            converted_pts.append([x_map_big_small[pt[0]],y_map_big_small[pt[1]]])
        grid = [[-1 for _ in range(x_max)] for _ in range(y_max)]
        
        for i in range(len(converted_pts)):
            pt = converted_pts[i]
            grid[pt[1]][pt[0]] = 1
            j = i+1
            if j == len(converted_pts):
                j = 0
            nxt = converted_pts[j]
            if nxt[0] == pt[0]:
                for y in range(min(pt[1],nxt[1]), max(pt[1],nxt[1]) + 1):
                    grid[y][pt[0]] = 1
            else:
                for x in range(min(pt[0],nxt[0]), max(pt[0],nxt[0]) + 1):
                    grid[pt[1]][x] = 1
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

        print_grid(grid)
        print()
        print_grid(prefix_grid)
        print(converted_pts)
        for i in range(len(converted_pts)):
            for j in range(len(converted_pts)):
                if i >= j:
                    continue
                pt1 = converted_pts[i]
                pt2 = converted_pts[j]
                # Ensure top-left and bottom-right corners
                top_left = [min(pt1[0], pt2[0]), min(pt1[1], pt2[1])]
                bottom_right = [max(pt1[0], pt2[0]), max(pt1[1], pt2[1])]
                prefix_area = rect_prefix_area(prefix_grid, top_left, bottom_right)
                rect_size = size(top_left, bottom_right)
                if prefix_area == rect_size:
                    cpt1 = [x_map[pt1[0]], y_map[pt1[1]]]
                    cpt2 = [x_map[pt2[0]], y_map[pt2[1]]]
                    result = max(result, size(cpt1,cpt2))
                
    return result


if __name__ == "__main__":
    print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))