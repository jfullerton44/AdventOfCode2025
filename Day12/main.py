"""Advent of Code 2025 - Day 12"""

from pathlib import Path

INPUT_FILE: Path = Path(__file__).parent / "input.txt"


def parse_input(file_path: Path) -> tuple[list[set[tuple[int, int]]], list[tuple[int, int, list[int]]]]:
    """Parse the input file and return shapes and regions.
    
    Returns:
        shapes: List of sets, each containing (row, col) coordinates of '#' cells
        regions: List of (width, height, counts) tuples where counts is list of shape quantities
    """
    shapes: list[set[tuple[int, int]]] = []
    regions: list[tuple[int, int, list[int]]] = []
    
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")
    
    current_shape: set[tuple[int, int]] = set()
    row = 0
    parsing_shapes = True
    
    for line in lines:
        if not line:
            continue
            
        # Check if this is a region line (contains 'x' and ':')
        if "x" in line and ":" in line and line[0].isdigit():
            parsing_shapes = False
            parts = line.split(": ")
            dimensions = parts[0].split("x")
            width = int(dimensions[0])
            height = int(dimensions[1])
            counts = [int(x) for x in parts[1].split()]
            regions.append((width, height, counts))
        elif parsing_shapes:
            if ":" in line:
                # New shape starting (e.g., "0:")
                if current_shape:
                    shapes.append(current_shape)
                current_shape = set()
                row = 0
            else:
                # Part of current shape
                for col, char in enumerate(line):
                    if char == "#":
                        current_shape.add((row, col))
                row += 1
    
    if current_shape:
        shapes.append(current_shape)
    
    return shapes, regions





def can_fit_by_area(shapes: list[set[tuple[int, int]]], width: int, height: int, counts: list[int]) -> bool:
    """Check if the total area of all packages is <= the region area.
    
    This is a necessary (but not sufficient) condition for fitting all packages.
    """
    region_area = width * height
    total_package_area = 0
    
    for shape_idx, count in enumerate(counts):
        if count > 0:
            shape_area = len(shapes[shape_idx])
            total_package_area += shape_area * count
    
    return total_package_area <= region_area


def solve_part1() -> int:
    """Solve part 1: Count regions that can fit all their presents.
    
    Just checking if total package area <= region area.
    """
    shapes, regions = parse_input(INPUT_FILE)
    result = 0
    
    for width, height, counts in regions:
        region_area = width * height
        total_package_area = sum(len(shapes[i]) * c for i, c in enumerate(counts) if c > 0)
        fits = total_package_area <= region_area
        print(f"Region {width}x{height}: area={region_area}, packages need {total_package_area} -> {'FITS' if fits else 'NO FIT'}")
        if fits:
            result += 1
    
    return result


def solve_part2():
    return "No part 2 on Day 12"


if __name__ == "__main__":
    print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))