"""Advent of Code 2025 - Day X"""

from collections import deque
from pathlib import Path
from typing import NamedTuple

INPUT_FILE = Path(__file__).parent / "input.txt"

class Item(NamedTuple):
    values: tuple
    count: int

def get_action_length(actions, result) -> int:
    queue = []
    seen = set()
    queue.append(Item(result,0))
    while len(queue) > 0:
        curr = queue.pop(0)
        for action in actions:
            new_values = [a ^ b for a, b in zip(action, curr.values)]
            if tuple(new_values) in seen:
                continue
            seen.add(tuple(new_values))
            if not any(new_values):
                print(curr.count + 1)
                return curr.count + 1
            else:
                queue.append(Item(new_values, curr.count + 1))
    

def solve_part1() -> int:
    answer = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            print(line)
            line = line.strip()
            parts = line.split(" ")
            res = parts[0]
            result = []
            for i in range(1, len(res)-1):
                if res[i] == ".":
                    result.append(False)
                else:
                    result.append(True)
            actions = []
            for i in range(1, len(parts)):
                temp = [False for _ in range(len(result))]
                chars = parts[i]
                if chars[0] == "{":
                    continue
                chars = chars[1:-1]
                nums = chars.split(",")
                for num in nums:
                    temp[int(num)] = True
                actions.append(temp)
            answer += get_action_length(actions, result)

    return answer

def get_action_length_int_jolts(actions: list[tuple], result: tuple) -> int:
    import heapq
    # Priority queue: (heuristic + count, count, values)
    # Heuristic is sum of all values
    heap = [(sum(result), 0, result)]
    seen = set()
    seen.add(result)
    
    while heap:
        _, count, values = heapq.heappop(heap)
        
        for action in actions:
            new_values = tuple(a - b for a, b in zip(values, action))
            if new_values in seen:
                continue
            seen.add(new_values)
            min_val = min(new_values)
            if min_val < 0:
                continue
            total = sum(new_values)
            if total == 0:
                print(count + 1)
                return count + 1
            priority = total + (count + 1)
            heapq.heappush(heap, (priority, count + 1, new_values))

def solve_part2() -> int:
    answer = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            print(line)
            line = line.strip()
            parts = line.split(" ")
            res = parts[-1]
            result = []
            chars = res[1:-1]
            nums = chars.split(",")
            for num in nums:
                result.append(int(num))
            result = tuple(result)
            actions = []
            for i in range(1, len(parts)-1):
                temp = [0 for _ in range(len(result))]
                chars = parts[i]
                chars = chars[1:-1]
                nums = chars.split(",")
                for num in nums:
                    temp[int(num)] = 1
                actions.append(tuple(temp))
            answer += get_action_length_int_jolts(actions, result)

    return answer


if __name__ == "__main__":
    print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))