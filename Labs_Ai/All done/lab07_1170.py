from queue import Queue, PriorityQueue
from time import time

# The Puzzle Node
class Puzzle:
    GOAL = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    count = 0

    def __init__(self, state, parent, action, cost, use_h=False):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = (parent.g + cost) if parent else 0
        self.h = self.manhattan() if use_h else 0
        self.f = self.g + self.h
        Puzzle.count += 1

    def is_goal(self):
        return self.state == Puzzle.GOAL

    # Heuristic: Manhattan Distance
    def manhattan(self):
        total = 0
        for i, val in enumerate(self.state):
            if val == 0:
                continue
            goal_idx = Puzzle.GOAL.index(val)
            total += abs(i // 3 - goal_idx // 3) + abs(i % 3 - goal_idx % 3)
        return total

    # Generate children
    def children(self):
        blank = self.state.index(0)
        row, col = divmod(blank, 3)

        moves = {
            'U': blank - 3,
            'D': blank + 3,
            'L': blank - 1,
            'R': blank + 1,
        }

        if row == 0:
            moves.pop('U')
        if row == 2:
            moves.pop('D')
        if col == 0:
            moves.pop('L')
        if col == 2:
            moves.pop('R')

        result = []
        for action, target in moves.items():
            new_state = self.state.copy()
            new_state[blank], new_state[target] = new_state[target], new_state[blank]
            result.append(Puzzle(new_state, self, action, 1, self.h > 0))
        return result

    # Get solution path
    def solution(self):
        path, node = [], self
        while node.parent:
            path.append(node.action)
            node = node.parent
        return list(reversed(path))


    # BFS Algorithm
    @staticmethod
    def bfs(start):
        frontier = Queue()
        explored = set()

        start_node = Puzzle(start, None, None, 0)
        frontier.put(start_node)
        explored.add(tuple(start))

        while not frontier.empty():
            node = frontier.get()

            if node.is_goal():
                return node.solution()

            for child in node.children():
                t = tuple(child.state)
                if t not in explored:
                    explored.add(t)
                    frontier.put(child)

    # A* Algorithm
    @staticmethod
    def astar(start):
        frontier = PriorityQueue()
        explored = set()
        counter = 0

        start_node = Puzzle(start, None, None, 0, use_h=True)
        frontier.put((start_node.f, counter, start_node))
        explored.add(tuple(start))

        while not frontier.empty():
            _, _, node = frontier.get()

            if node.is_goal():
                return node.solution()

            for child in node.children():
                t = tuple(child.state)
                if t not in explored:
                    explored.add(t)
                    counter += 1
                    frontier.put((child.f, counter, child))


# Run & Compare
states = [
    [1, 3, 4, 8, 6, 2, 7, 0, 5],
    [2, 8, 1, 0, 4, 3, 7, 6, 5],
    [2, 8, 1, 4, 6, 3, 0, 7, 5],
]

for state in states:
    print(f"Start: {state}")

    for name, fn in [("BFS", Puzzle.bfs), ("A*", Puzzle.astar)]:
        Puzzle.count = 0
        t = time()
        sol = fn(state)
        print(f" {name} → {sol} | nodes: {Puzzle.count} | time: {time()-t:.4f}s")

    print()