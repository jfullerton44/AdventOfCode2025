"""Advent of Code 2025 - Day 4."""

from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input.txt"


def is_valid(grid: list[list[str]], row: int, col: int) -> bool:
    """
    Check if a cell has 4 or fewer adjacent '@' symbols.

    Args:
        grid: The 2D grid of characters.
        row: Row index of the cell to check.
        col: Column index of the cell to check.

    Returns:
        True if the cell has 4 or fewer adjacent '@' symbols.
    """
    count = 0

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
                continue
            if grid[r][c] == "@":
                count += 1

    return count <= 4


def load_grid() -> list[list[str]]:
    """
    Load the grid from the input file.

    Returns:
        2D list of characters representing the grid.
    """
    grid = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            grid.append(list(line))

    return grid


def solve_part1() -> int:
    """
    Solve Part 1: Count valid '@' cells.

    Returns:
        Number of '@' cells with 4 or fewer adjacent '@' symbols.
    """
    grid = load_grid()
    result = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@" and is_valid(grid, i, j):
                result += 1

    return result


def solve_part2() -> int:
    """
    Solve Part 2: Iteratively remove valid '@' cells.

    Repeatedly find and remove '@' cells that have 4 or fewer
    adjacent '@' symbols until no more can be removed.

    Returns:
        Total number of '@' cells removed.
    """
    grid = load_grid()
    result = 0
    removed_count = -1

    while removed_count != 0:
        removed_count = 0
        cells_to_remove = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "@" and is_valid(grid, i, j):
                    result += 1
                    removed_count += 1
                    cells_to_remove.append((i, j))

        for row, col in cells_to_remove:
            grid[row][col] = "."

    return result


if __name__ == "__main__":
    print(f"Part 1: {solve_part1()}")
    print(f"Part 2: {solve_part2()}")