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
    """
    Solve using Z3 SMT solver.
    We need to find non-negative integers x such that A @ x = result,
    minimizing sum(x) (total number of actions).
    """
    from z3 import Int, Optimize, Sum, sat
    
    n_actions = len(actions)
    n_positions = len(result)
    
    # Create integer variables for how many times each action is used
    x = [Int(f'x_{i}') for i in range(n_actions)]
    
    # Create optimizer
    opt = Optimize()
    
    # Constraints: x[i] >= 0
    for i in range(n_actions):
        opt.add(x[i] >= 0)
    
    # Constraints: for each position, sum of actions covering it = target
    for pos in range(n_positions):
        opt.add(Sum([x[i] * actions[i][pos] for i in range(n_actions)]) == result[pos])
    
    # Minimize total actions
    opt.minimize(Sum(x))
    
    if opt.check() == sat:
        model = opt.model()
        total = sum(model[x[i]].as_long() for i in range(n_actions))
        return total
    else:
        print("No solution")
        return -1

def solve_part2() -> int:
    answer = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            # print(line)
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