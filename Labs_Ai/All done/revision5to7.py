import collections
import matplotlib.pyplot as plt
import networkx as nx
import random
from queue import Queue, PriorityQueue
from time import time

# print("="*50)
# print("Q1: City Road Network")
# print("="*50)

# class Graph:
#     def __init__(self):
#         self.edges = {}

#     def addVertex(self, vertex):
#         if vertex not in self.edges:
#             self.edges[vertex] = []

#     def addEdge(self, vertex1, vertex2):
#         if vertex1 in self.edges and vertex2 in self.edges:
#             if vertex2 not in self.edges[vertex1]:
#                 self.edges[vertex1].append(vertex2)
#             if vertex1 not in self.edges[vertex2]:
#                 self.edges[vertex2].append(vertex1)

#     def printEdges(self):
#         for vertex, neighbors in self.edges.items():
#             print(f"{vertex}: {neighbors}")

#     def visualize(self):
#         g = nx.Graph()
#         for node, neighbors in self.edges.items():
#             g.add_node(node)
#             for neighbor in neighbors:
#                 g.add_edge(node, neighbor)
        
#         plt.figure(figsize=(6, 4))
#         nx.draw(g, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
#         plt.title("City Road Network")
#         plt.show(block=False)
#         plt.pause(20)
#         plt.close()


# graph = Graph()
# cities = ["New York", "Boston", "Chicago", "Denver", "Seattle", "San Francisco"]
# for city in cities:
#     graph.addVertex(city)

# graph.addEdge("New York", "Boston")
# graph.addEdge("New York", "Chicago")
# graph.addEdge("Chicago", "Denver")
# graph.addEdge("Denver", "Seattle")
# graph.addEdge("Denver", "San Francisco")
# graph.addEdge("Seattle", "San Francisco")

# graph.printEdges()
# graph.visualize()



# print("\n" + "="*50)
# print("Q2: BFS and DFS on Romania Map")
# print("="*50)

# romania = {
#     'sibiu': ['Fagaras', 'rimnicu', 'Vilcea'],
#     'Fagaras': ['Bucharest'],
#     'Rimnicu Vilcea': ["Pitesti"],
#     'Pitesti': ['Bucharest'],
#     'rimnicu': ['Pitesti'], # Added linking based on common map or typo
#     'Vilcea': ['Pitesti'],  
#     'Bucharest': []
# }

# def breadth_first(start, goal, neighbors_dict):
#     frontier = [start]
#     previous = {start: None}
#     while frontier:
#         current = frontier.pop(0)
#         if current == goal:
#             path = []
#             while current is not None:
#                 path.append(current)
#                 current = previous[current]
#             return path[::-1]
#         for neighbor in neighbors_dict.get(current, []):
#             if neighbor not in previous:
#                 previous[neighbor] = current
#                 frontier.append(neighbor)
#     return None



# def depth_first(start, goal, neighbors_dict):
#     frontier = [start]
#     previous = {start: None}
#     while frontier:
#         current = frontier.pop()
#         if current == goal:
#             path = []
#             while current is not None:
#                 path.append(current)
#                 current = previous[current]
#             return path[::-1]
#         for neighbor in neighbors_dict.get(current, []):
#             if neighbor not in previous:
#                 previous[neighbor] = current
#                 frontier.append(neighbor)
#     return None

# start_state = 'sibiu'
# goal_state = 'Bucharest'

# result_bfs = breadth_first(start_state, goal_state, romania)
# result_dfs = depth_first(start_state, goal_state, romania)
# print("Breadth-First Search Path:", result_bfs)
# print("Depth-First Search Path:", result_dfs)
# print("Explanation: BFS explores level by level, finding the shortest path in terms of edges. DFS dives deep into the graph before backtracking, which can lead to a longer or different path if multiple paths exist and it explores a longer branch first.")




# print("\n" + "="*50)
# print("Q3: NIM Game (AI starts, 15 counters)")
# print("="*50)

# def initial_state():
#     return random.randint(1, 10)

# def possible_new_states(state):
#     return [state - take for take in (1, 2, 3) if take <= state]

# def evaluate(state, is_maximizing):
#     if state == 0:
#         return 1 if is_maximizing else -1
#     return None

# def minimax(state, is_maximizing):
#     score = evaluate(state, is_maximizing)
#     if score is not None:
#         return score

#     moves = [
#         minimax(new_state, not is_maximizing)
#         for new_state in possible_new_states(state)
#     ]
#     return max(moves) if is_maximizing else min(moves)

# def best_move(state):
#     # Determine the best move for the AI using minimax
#     # The AI is maximizing
#     best_score = -float('inf')
#     best_next_state = None
    
#     for next_state in possible_new_states(state):
#         score = minimax(next_state, False)
#         if score > best_score:
#             best_score = score
#             best_next_state = next_state
            
#     return best_next_state

# def play_nim():
#     while True:
#         state = initial_state()
#         print(f"Starting NIM game with {state} counters.")
#         while state > 0:
#             # AI's Turn
#             print(f"\nCurrent counters: {state}")
#             print("AI's turn...")
#             ai_move = best_move(state)
#             print(f"AI takes {state - ai_move} counter(s).")
#             state = ai_move
            
#             if state == 0:
#                 print("AI took the last counter! AI wins!")
#                 break
                
#             # Human's Turn
#             print(f"\nCurrent counters: {state}")
#             while True:
#                 try:
#                     take = int(input("How many counters do you want to take (1, 2, or 3)? "))
#                     if take in (1, 2, 3) and take <= state:
#                         break
#                     else:
#                         print("Invalid move. Try again.")
#                 except ValueError:
#                     print("Please enter a number.")
#             state -= take
            
#             if state == 0:
#                 print("You took the last counter! You win!")
#                 break
                
#         replay = input("\nDo you want to play again? (y/n): ").strip().lower()
#         if replay != 'y':
#             break

# # Temporarily disabled automatic input for testing purposes
# # play_nim() 
# print("NIM Game properly structured. Uncomment play_nim() at the bottom to play.")



print("\n" + "="*50)
print("Q4: 8-Puzzle using A* and BFS")
print("="*50)

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
    
    def manhattan(self):
        total = 0
        for i, val in enumerate(self.state):
            if val == 0:
                continue
            goal_idx = Puzzle.GOAL.index(val)
            total += abs(i // 3 - goal_idx // 3) + abs(i % 3 - goal_idx % 3)
        return total
    
    def children(self):
        blank = self.state.index(0)
        row, col = divmod(blank, 3)
        moves = {
            'U': blank - 3,
            'D': blank + 3,
            'L': blank - 1,
            'R': blank + 1,
        }
        
        if row == 0: del moves['U']
        if row == 2: del moves['D']
        if col == 0: del moves['L']
        if col == 2: del moves['R']
        
        result = []
        for action, target in moves.items():
            s = self.state.copy()
            s[blank], s[target] = s[target], s[blank]
            result.append(Puzzle(s, self, action, 1, self.h > 0))
        return result
    
    def solution(self):
        path, node = [], self
        while node.parent:
            path.append(node.action)
            node = node.parent
        return list(reversed(path))

def bfs_puzzle(start_state):
    Puzzle.count = 0
    start_node = Puzzle(start_state, None, None, 0)
    frontier = [start_node]
    explored = set()
    
    while frontier:
        node = frontier.pop(0)
        
        if node.is_goal():
            return node.solution(), Puzzle.count
            
        explored.add(tuple(node.state))
        
        for child in node.children():
            if tuple(child.state) not in explored:
                # Add to frontier avoiding duplicates in simple way
                is_in_frontier = False
                for f_node in frontier:
                    if f_node.state == child.state:
                        is_in_frontier = True
                        break
                if not is_in_frontier:
                    frontier.append(child)
    return None, Puzzle.count

def astar_puzzle(start_state):
    Puzzle.count = 0
    counter = 0
    start_node = Puzzle(start_state, None, None, 0, use_h=True)
    frontier = PriorityQueue()
    frontier.put((start_node.f, counter, start_node))
    explored = set()
    
    while not frontier.empty():
        _, _, node = frontier.get()
        
        if node.is_goal():
            return node.solution(), Puzzle.count
            
        explored.add(tuple(node.state))
        
        for child in node.children():
            if tuple(child.state) not in explored:
                counter += 1
                frontier.put((child.f, counter, child))
    return None, Puzzle.count

start_state_8_puzzle = [2, 8, 1, 0, 4, 3, 7, 6, 5]

print(f"Start State: {start_state_8_puzzle}")
print(f"Goal State:  {Puzzle.GOAL}")

t0 = time()
path_astar, nodes_astar = astar_puzzle(start_state_8_puzzle)
time_astar = time() - t0

t0 = time()
path_bfs, nodes_bfs = bfs_puzzle(start_state_8_puzzle)
time_bfs = time() - t0

print(f"\nA* Search:")
print(f"Sequence of moves: {path_astar}")
print(f"Total nodes explored: {nodes_astar}")
print(f"Time taken: {time_astar:.4f}s")

print(f"\nBFS Search:")
print(f"Sequence of moves: {path_bfs}")
print(f"Total nodes explored: {nodes_bfs}")
print(f"Time taken: {time_bfs:.4f}s")

print("\nComparison:")
print(f"BFS explored {nodes_bfs} nodes vs A* explored {nodes_astar} nodes.")
print("The Manhattan heuristic helps A* by estimating the cost to reach the goal from the current state. This allows A* to prioritize exploring paths that appear to lead more directly to the goal, significantly reducing the number of nodes it needs to explore compared to the blind approach of BFS.")

if __name__ == "__main__":
    # To play NIM game, uncomment the following line:
    # play_nim()
    pass