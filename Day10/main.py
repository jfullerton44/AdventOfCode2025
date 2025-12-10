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
    
    # Better heuristic: max value (minimum steps needed since each position decreases by at most 1 per step)
    def heuristic(values):
        return sum(values) + max(values) * 5 if values else 0
    
    # Priority queue: (f_score, count, values)
    # f_score = count + heuristic
    initial_h = heuristic(result)
    heap = [(initial_h, 0, result)]
    # Track best cost to reach each state
    best_cost = {result: 0}
    
    while heap:
        f, count, values = heapq.heappop(heap)
        
        # Skip if we've found a better path to this state
        if count > best_cost.get(values, float('inf')):
            continue
        
        for action in actions:
            new_values = tuple(a - b for a, b in zip(values, action))
            
            # Prune negative values early
            min_val = min(new_values)
            if min_val < 0:
                continue
            
            new_count = count + 1
            
            # Only process if this is a better path to new_values
            if new_count >= best_cost.get(new_values, float('inf')):
                continue
            best_cost[new_values] = new_count
            
            # Check for goal
            max_val = max(new_values)
            if max_val == 0:
                print(new_count)
                return new_count
            
            # f = g + h where g = new_count, h = max(new_values)
            priority = new_count + heuristic(new_values)
            heapq.heappush(heap, (priority, new_count, new_values))

def solve_part2() -> int:
    answer = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            print(line)
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
    #print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))