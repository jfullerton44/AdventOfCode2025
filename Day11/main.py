"""Advent of Code 2025 - Day 11"""

from collections import deque
from dataclasses import dataclass, field
from pathlib import Path

INPUT_FILE: Path = Path(__file__).parent / "input.txt"


@dataclass
class Generator:
    """Represents a generator node with connections to other generators."""
    id: int
    next_gens: list[int] = field(default_factory=list)

def parse_input(file_path: Path) -> tuple[dict[str, int], dict[int, str], list[Generator]]:
    """Parse the input file and return letter map, id-to-name map, and generators."""
    letter_map: dict[str, int] = {}
    id_to_name: dict[int, str] = {}
    generators: list[Generator] = []
    curr: int = 0

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            splits: list[str] = line.split(":")
            name: str = splits[0]

            if name not in letter_map:
                letter_map[name] = curr
                id_to_name[curr] = name
                gen = Generator(curr)
                generators.append(gen)
                curr += 1

            gen = generators[letter_map[name]]
            connections: list[str] = splits[1].strip().split(" ")

            for connection in connections:
                if connection not in letter_map:
                    letter_map[connection] = curr
                    id_to_name[curr] = connection
                    t_gen = Generator(curr)
                    generators.append(t_gen)
                    curr += 1
                gen.next_gens.append(letter_map[connection])

    return letter_map, id_to_name, generators


def solve_part1() -> int:
    """Solve part 1: Count all paths from 'you' to 'out'."""
    letter_map, _, generators = parse_input(INPUT_FILE)
    result: int = 0

    start: int = letter_map["you"]
    end: int = letter_map["out"]

    queue: deque[int] = deque()
    queue.append(start)

    while queue:
        item: int = queue.popleft()
        gen: Generator = generators[item]
        for conn in gen.next_gens:
            if conn == end:
                result += 1
            else:
                queue.append(conn)

    return result


def solve_part2() -> int:
    """Solve part 2: Count paths from 'svr' to 'out' that pass through both 'fft' and 'dac'.
    """
    letter_map, _, generators = parse_input(INPUT_FILE)

    start: int = letter_map["svr"]
    end: int = letter_map["out"]
    fft_id: int = letter_map["fft"]
    dac_id: int = letter_map["dac"]

    # Memoization cache: (node, has_fft, has_dac) -> count of valid paths to end
    memo: dict[tuple[int, bool, bool], int] = {}

    def dfs(node: int, has_fft: bool, has_dac: bool) -> int:
        """Recursively count valid paths from node to end."""
        if node == end:
            return 1 if (has_fft and has_dac) else 0

        state = (node, has_fft, has_dac)
        if state in memo:
            return memo[state]

        count = 0
        gen: Generator = generators[node]

        for conn in gen.next_gens:
            new_fft = has_fft or conn == fft_id
            new_dac = has_dac or conn == dac_id
            count += dfs(conn, new_fft, new_dac)

        memo[state] = count
        return count

    return dfs(start, start == fft_id, start == dac_id)


if __name__ == "__main__":
    print("Part 1: " + str(solve_part1()))
    print(f"Part 2: {solve_part2()}")