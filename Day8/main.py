"""Advent of Code 2025 - Day 8"""

from pathlib import Path
import queue

INPUT_FILE = Path(__file__).parent / "input.txt"

class Node:
    def __init__(self, id, pos):
        self.id = id
        coord = pos.split(",")
        self.x = int(coord[0])
        self.y = int(coord[1])
        self.z = int(coord[2])
        self.connections = set()
    
    def is_connected(self, id):
        q = []
        seen = set()
        seen.add(self.id)  # Add self to seen initially
        for item in self.connections:
            q.append(item)
            seen.add(item.id)
        while len(q) > 0:
            curr = q.pop(0)
            if curr.id == id:
                return True
            for conn in curr.connections:
                if conn.id not in seen:
                    seen.add(conn.id)
                    q.append(conn)
        return False
    
    def distance(self, node):
        x_dist = pow(self.x - node.x,2)
        y_dist = pow(self.y - node.y,2)
        z_dist = pow(self.z - node.z,2)

        return pow(x_dist + y_dist + z_dist, .5)

    def connection_size(self, seen):
        if self.id in seen:
            return 0
        # BFS to count all nodes in this connected component
        size = 0
        q = [self]
        seen.add(self.id)
        while len(q) > 0:
            curr = q.pop(0)
            size += 1
            for conn in curr.connections:
                if conn.id not in seen:
                    seen.add(conn.id)
                    q.append(conn)
        return size
                



def solve_part1() -> int:
    result = 0
    nodes = []
    pq = queue.PriorityQueue()
    with open(INPUT_FILE, "r") as file:
        i = 0
        for line in file:
            line = line.strip()
            nodes.append(Node(i, line))
            i += 1
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i == j or j > i:
                continue
            distance = nodes[i].distance(nodes[j])
            pq.put((distance, (i, j)))

    for n in range(1000):
        connection = pq.get()[1]
        # Only add connection if not already connected (but still count it as one of our 10)
        if not nodes[connection[0]].is_connected(nodes[connection[1]].id):
            nodes[connection[0]].connections.add(nodes[connection[1]])
            nodes[connection[1]].connections.add(nodes[connection[0]])


    seen = set()
    sizes = []
    for node in nodes:
        size = node.connection_size(seen)
        if size != 0:
            sizes.append(size)
    
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

def solve_part2() -> int:
    result = 0
    nodes = []
    pq = queue.PriorityQueue()
    with open(INPUT_FILE, "r") as file:
        i = 0
        for line in file:
            line = line.strip()
            nodes.append(Node(i, line))
            i += 1
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i == j or j > i:
                continue
            distance = nodes[i].distance(nodes[j])
            pq.put((distance, (i, j)))

    sizes = []

    for n in range(1000):
        connection = pq.get()[1]
        # Only add connection if not already connected (but still count it as one of our 10)
        if not nodes[connection[0]].is_connected(nodes[connection[1]].id):
            nodes[connection[0]].connections.add(nodes[connection[1]])
            nodes[connection[1]].connections.add(nodes[connection[0]])
    seen = set()
    sizes = []
    for node in nodes:
        size = node.connection_size(seen)
        if size != 0:
            sizes.append(size)
    while len(sizes) > 2:
        connection = pq.get()[1]
        # Only add connection if not already connected (but still count it as one of our 10)
        if not nodes[connection[0]].is_connected(nodes[connection[1]].id):
            nodes[connection[0]].connections.add(nodes[connection[1]])
            nodes[connection[1]].connections.add(nodes[connection[0]])
            seen = set()
            sizes = []
            for node in nodes:
                size = node.connection_size(seen)
                if size != 0:
                    sizes.append(size)

    connection = pq.get()[1]
    while  nodes[connection[0]].is_connected(nodes[connection[1]].id):
        connection = pq.get()[1]
    return nodes[connection[0]].x * nodes[connection[1]].x


if __name__ == "__main__":
    print("Part 1: " + str(solve_part1()))
    print("Part 2: " + str(solve_part2()))