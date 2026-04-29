# =============================================================================
# 15-PUZZLE GAME - Beautiful Blue/Black UI Theme (4x4 Only)
# =============================================================================

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import heapq
import time
from collections import deque

# =============================================================================
# Board size options & Constants
# =============================================================================
SIZE = 4  # Fixed to 4x4 for 15-puzzle
DEPTH_LIMIT_DFS = 50  # Depth limit for DFS on 4x4
NODE_LIMIT_BFS = 500000   # 500k nodes limit for BFS
NODE_LIMIT_DFS = 200000   # 200k nodes limit for DFS
GOAL_STATE = list(range(1, 16)) + [0]  # 1-15 then 0 for blank tile


# =============================================================================
# Puzzle Board Logic
# =============================================================================
class PuzzleBoard:
    """Represents the 15‑puzzle board and its operations."""
    
    def __init__(self):
        self.size = SIZE
        self.tiles = GOAL_STATE[:]          # start solved
        self.blank_pos = len(self.tiles) - 1   # last position (0)
    
    def copy(self):
        """Return a deep copy of the board."""
        new_board = PuzzleBoard()
        new_board.tiles = self.tiles[:]
        new_board.blank_pos = self.blank_pos
        return new_board
    
    def get_inversions(self):
        """Count inversions (ignoring blank)."""
        inv = 0
        arr = [t for t in self.tiles if t != 0]
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    inv += 1
        return inv
    
    def is_solvable(self):
        """Check if the current arrangement is solvable for 4x4."""
        inv = self.get_inversions()
        blank_row_from_bottom = self.size - (self.blank_pos // self.size)
        return (inv % 2 == 0) == (blank_row_from_bottom % 2 == 1)
    
    def get_neighbors(self):
        """Return list of possible moves (tile numbers) and the resulting boards."""
        row, col = divmod(self.blank_pos, self.size)
        moves = []
        # Up, Down, Left, Right
        if row > 0: moves.append(('up', self.blank_pos - self.size))
        if row < self.size-1: moves.append(('down', self.blank_pos + self.size))
        if col > 0: moves.append(('left', self.blank_pos - 1))
        if col < self.size-1: moves.append(('right', self.blank_pos + 1))
        
        neighbors = []
        for direction, pos in moves:
            new_board = self.copy()
            tile_moved = new_board.tiles[pos]
            # Swap blank with tile
            new_board.tiles[self.blank_pos], new_board.tiles[pos] = new_board.tiles[pos], 0
            new_board.blank_pos = pos
            neighbors.append((tile_moved, new_board))
        return neighbors
    
    def shuffle(self, num_moves=100):
        """Guaranteed solvable shuffle by simulating random moves."""
        self.tiles = GOAL_STATE[:]
        self.blank_pos = len(self.tiles) - 1
        for _ in range(num_moves):
            neighbors = self.get_neighbors()
            if neighbors:
                _, board = random.choice(neighbors)
                self.tiles = board.tiles
                self.blank_pos = board.blank_pos
    
    def move_tile(self, tile_num):
        """Move a tile if adjacent to blank. Returns True if moved."""
        if tile_num == 0:
            return False
        try:
            tile_idx = self.tiles.index(tile_num)
        except ValueError:
            return False
        row_tile, col_tile = divmod(tile_idx, self.size)
        row_blank, col_blank = divmod(self.blank_pos, self.size)
        if abs(row_tile - row_blank) + abs(col_tile - col_blank) == 1:
            # Swap
            self.tiles[tile_idx], self.tiles[self.blank_pos] = self.tiles[self.blank_pos], self.tiles[tile_idx]
            self.blank_pos = tile_idx
            return True
        return False
    
    def is_solved(self):
        return self.tiles == GOAL_STATE


# =============================================================================
# Search Algorithms (BFS, DFS, A*)
# =============================================================================
class Solver:
    """Collection of static methods for solving the puzzle."""
    
    @staticmethod
    def bfs(initial_board, node_limit=NODE_LIMIT_BFS):
        """Breadth‑First Search with node limit. Returns (moves_list, nodes_expanded, elapsed_time, reached_limit)."""
        start_time = time.time()
        queue = deque()
        queue.append((initial_board.copy(), []))   # (board, path_of_moves)
        visited = set()
        visited.add(tuple(initial_board.tiles))
        nodes_expanded = 0
        reached_limit = False
        
        while queue:
            board, path = queue.popleft()
            nodes_expanded += 1
            
            # Check node limit
            if nodes_expanded > node_limit:
                reached_limit = True
                elapsed = time.time() - start_time
                return None, nodes_expanded, elapsed, reached_limit
            
            if board.is_solved():
                elapsed = time.time() - start_time
                return path, nodes_expanded, elapsed, reached_limit
            
            for tile, neighbor in board.get_neighbors():
                state = tuple(neighbor.tiles)
                if state not in visited:
                    visited.add(state)
                    queue.append((neighbor, path + [tile]))
        
        elapsed = time.time() - start_time
        return None, nodes_expanded, elapsed, reached_limit
    
    @staticmethod
    def dfs_limited(initial_board, depth_limit, node_limit=NODE_LIMIT_DFS):
        """Depth‑limited DFS with node limit. Returns (moves, nodes_expanded, elapsed, reached_limit)."""
        start_time = time.time()
        visited = set()
        visited.add(tuple(initial_board.tiles))
        nodes_expanded = 0
        reached_limit = False
        
        def dfs(board, path, depth):
            nonlocal nodes_expanded, reached_limit
            nodes_expanded += 1
            
            # Check node limit
            if nodes_expanded > node_limit:
                reached_limit = True
                return None
            
            if board.is_solved():
                return path
            if depth >= depth_limit:
                return None
            for tile, neighbor in board.get_neighbors():
                state = tuple(neighbor.tiles)
                if state not in visited:
                    visited.add(state)
                    result = dfs(neighbor, path + [tile], depth + 1)
                    if result is not None:
                        return result
                    if reached_limit:
                        return None
            return None
        
        result = dfs(initial_board, [], 0)
        elapsed = time.time() - start_time
        return result, nodes_expanded, elapsed, reached_limit
    
    @staticmethod
    def a_star(initial_board, heuristic_func):
        """A* search. heuristic_func(board) returns h-value."""
        start_time = time.time()
        counter = 0
        open_list = []
        start_board = initial_board.copy()
        heapq.heappush(open_list, (0, counter, 0, start_board, []))
        closed = set()
        nodes_expanded = 0
        
        while open_list:
            f, _, g, board, path = heapq.heappop(open_list)
            state = tuple(board.tiles)
            
            if state in closed:
                continue
            closed.add(state)
            nodes_expanded += 1
            
            if board.is_solved():
                elapsed = time.time() - start_time
                return path, nodes_expanded, elapsed
            
            for tile, neighbor in board.get_neighbors():
                n_state = tuple(neighbor.tiles)
                if n_state not in closed:
                    new_g = g + 1
                    h = heuristic_func(neighbor)
                    new_f = new_g + h
                    counter += 1
                    heapq.heappush(open_list, (new_f, counter, new_g, neighbor, path + [tile]))
        
        elapsed = time.time() - start_time
        return None, nodes_expanded, elapsed


# Heuristic functions
def heuristic_misplaced(board):
    """h₁: number of misplaced tiles (excluding blank)."""
    goal = GOAL_STATE
    return sum(1 for i, t in enumerate(board.tiles) if t != 0 and t != goal[i])

def heuristic_manhattan(board):
    """h₂: sum of Manhattan distances for each tile to its goal position."""
    size = board.size
    distance = 0
    for i, tile in enumerate(board.tiles):
        if tile == 0:
            continue
        goal_idx = tile - 1
        goal_row, goal_col = divmod(goal_idx, size)
        curr_row, curr_col = divmod(i, size)
        distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance


# =============================================================================
# Algorithm Comparison Runner
# =============================================================================
def compare_algorithms(board):
    """Run all solvers on a copy of the board and return a dictionary of results."""
    results = {}
    print("Running BFS...")
    moves, nodes, t, limit_reached = Solver.bfs(board.copy())
    results["BFS"] = {"moves": moves, "nodes": nodes, "time": t, "length": len(moves) if moves else None, "limit_reached": limit_reached}
    
    print("Running DFS (depth-limited)...")
    moves, nodes, t, limit_reached = Solver.dfs_limited(board.copy(), DEPTH_LIMIT_DFS)
    results["DFS"] = {"moves": moves, "nodes": nodes, "time": t, "length": len(moves) if moves else None, "limit_reached": limit_reached}
    
    print("Running A* (h1 = Misplaced)...")
    moves, nodes, t = Solver.a_star(board.copy(), heuristic_misplaced)
    results["A* (h1)"] = {"moves": moves, "nodes": nodes, "time": t, "length": len(moves) if moves else None, "limit_reached": False}
    
    print("Running A* (h2 = Manhattan)...")
    moves, nodes, t = Solver.a_star(board.copy(), heuristic_manhattan)
    results["A* (h2)"] = {"moves": moves, "nodes": nodes, "time": t, "length": len(moves) if moves else None, "limit_reached": False}
    
    return results


# =============================================================================
# 15-Puzzle GUI with Beautiful Blue/Black UI Theme (4x4 Only, Responsive)
# =============================================================================
class PuzzleGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("15-Puzzle Solver")
        self.window.configure(bg='#0a0a1a')
        self.board = PuzzleBoard()
        self.board.shuffle(100)
        self.move_counter = 0
        
        # Configure window size - make it responsive
        self.window.geometry("900x700")
        self.window.minsize(600, 550)
        
        # Title Frame
        title_frame = tk.Frame(self.window, bg='#0a0a1a')
        title_frame.pack(pady=15)
        title_label = tk.Label(title_frame, text="15-PUZZLE", font=("Segoe UI", 28, "bold"),
                              fg='#4a9eff', bg='#0a0a1a')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Slide the tiles to solve the puzzle (4x4)", 
                                 font=("Segoe UI", 12), fg='#888888', bg='#0a0a1a')
        subtitle_label.pack()
        
        # Control Frame
        control_frame = tk.Frame(self.window, bg='#0a0a1a')
        control_frame.pack(pady=20)
        
        # Board Size Label
        size_frame = tk.Frame(control_frame, bg='#0a0a1a')
        size_frame.pack(side=tk.LEFT, padx=15)
        
        size_label = tk.Label(size_frame, text="Board Size: 4x4", font=("Segoe UI", 11, "bold"),
                             fg='#4a9eff', bg='#0a0a1a')
        size_label.pack(side=tk.LEFT, padx=5)
        
        # Separator
        sep = tk.Frame(control_frame, width=2, height=30, bg='#2a2a4a')
        sep.pack(side=tk.LEFT, padx=10)
        
        # Action buttons
        action_frame = tk.Frame(control_frame, bg='#0a0a1a')
        action_frame.pack(side=tk.LEFT, padx=20)
        
        shuffle_btn = tk.Button(action_frame, text="🔀 Shuffle", font=("Segoe UI", 10, "bold"),
                               bg='#0f3460', fg='white', activebackground='#1a4a7a',
                               relief=tk.FLAT, bd=0, padx=15, pady=5, command=self.shuffle_board)
        shuffle_btn.pack(side=tk.LEFT, padx=4)
        
        # Separator
        sep2 = tk.Frame(control_frame, width=2, height=30, bg='#2a2a4a')
        sep2.pack(side=tk.LEFT, padx=10)
        
        # Solve buttons
        solve_frame = tk.Frame(control_frame, bg='#0a0a1a')
        solve_frame.pack(side=tk.LEFT)
        
        solve_bfs = tk.Button(solve_frame, text="BFS Solve", font=("Segoe UI", 9, "bold"),
                             bg='#1a3a5a', fg='white', activebackground='#2a4a7a',
                             relief=tk.FLAT, bd=0, padx=10, pady=5, command=lambda: self.solve('bfs'))
        solve_bfs.pack(side=tk.LEFT, padx=3)
        
        solve_dfs = tk.Button(solve_frame, text="DFS Solve", font=("Segoe UI", 9, "bold"),
                             bg='#1a3a5a', fg='white', activebackground='#2a4a7a',
                             relief=tk.FLAT, bd=0, padx=10, pady=5, command=lambda: self.solve('dfs'))
        solve_dfs.pack(side=tk.LEFT, padx=3)
        
        solve_a1 = tk.Button(solve_frame, text="A* (Misplaced)", font=("Segoe UI", 9, "bold"),
                            bg='#1a5a3a', fg='white', activebackground='#2a7a4a',
                            relief=tk.FLAT, bd=0, padx=10, pady=5, command=lambda: self.solve('a_star_h1'))
        solve_a1.pack(side=tk.LEFT, padx=3)
        
        solve_a2 = tk.Button(solve_frame, text="A* (Manhattan)", font=("Segoe UI", 9, "bold"),
                            bg='#1a5a3a', fg='white', activebackground='#2a7a4a',
                            relief=tk.FLAT, bd=0, padx=10, pady=5, command=lambda: self.solve('a_star_h2'))
        solve_a2.pack(side=tk.LEFT, padx=3)
        
        compare_btn = tk.Button(solve_frame, text="📊 Compare All", font=("Segoe UI", 9, "bold"),
                               bg='#5a2a3a', fg='white', activebackground='#7a3a5a',
                               relief=tk.FLAT, bd=0, padx=12, pady=5, command=self.compare_all)
        compare_btn.pack(side=tk.LEFT, padx=8)
        
        # Canvas Frame - Responsive
        canvas_frame = tk.Frame(self.window, bg='#1a1a2e', bd=3, relief=tk.RAISED)
        canvas_frame.pack(pady=20, fill=tk.BOTH, expand=True, padx=20)
        
        self.canvas = tk.Canvas(canvas_frame, bg='#0a0a1a', 
                                highlightthickness=0, bd=0)
        self.canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Bind resize event
        self.canvas.bind("<Configure>", self.on_canvas_resize)
        
        # Info Panel
        info_frame = tk.Frame(self.window, bg='#0a0a1a')
        info_frame.pack(pady=15)
        
        moves_label = tk.Label(info_frame, text="Moves:", font=("Segoe UI", 14, "bold"),
                              fg='#4a9eff', bg='#0a0a1a')
        moves_label.pack(side=tk.LEFT, padx=5)
        
        self.moves_value = tk.Label(info_frame, text="0", font=("Segoe UI", 16, "bold"),
                                    fg='#ffffff', bg='#0a0a1a')
        self.moves_value.pack(side=tk.LEFT, padx=10)
        
        self.status_indicator = tk.Label(info_frame, text="● Playing", font=("Segoe UI", 10),
                                         fg='#4a9eff', bg='#0a0a1a')
        self.status_indicator.pack(side=tk.LEFT, padx=20)
        
        self.draw_board()
    
    def on_canvas_resize(self, event):
        """Handle canvas resize event to redraw board"""
        self.draw_board()
    
    def shuffle_board(self):
        self.board.shuffle(100)
        self.move_counter = 0
        self.update_info()
        self.status_indicator.config(text="● Playing", fg='#4a9eff')
        self.draw_board()
    
    def draw_board(self):
        """Draw the board responsively based on canvas size"""
        self.canvas.delete("all")
        size = SIZE
        
        # Get current canvas dimensions
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width <= 1 or canvas_height <= 1:
            canvas_width = 500
            canvas_height = 500
        
        # Calculate tile size to fit canvas (use the smaller dimension)
        tile_size = min(canvas_width, canvas_height) // size
        
        # Calculate offset to center the board
        total_width = tile_size * size
        total_height = tile_size * size
        offset_x = (canvas_width - total_width) // 2
        offset_y = (canvas_height - total_height) // 2
        
        for i, tile in enumerate(self.board.tiles):
            row, col = divmod(i, size)
            x1 = offset_x + col * tile_size
            y1 = offset_y + row * tile_size
            x2 = x1 + tile_size
            y2 = y1 + tile_size
            
            if tile == 0:
                # Empty space (blank tile)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill='#1a1a2e', outline='#2a4a8a', width=2)
            else:
                # MATCHING YOUR SCREENSHOT COLORS - Dark muted blues and purples
                colors = [
                    '#2C3E6B', '#2D3F6E', '#2E4071', '#2F4174',  # Dark muted blues
                    '#304577', '#31467A', '#32477D', '#334880',  # Slightly lighter muted blues
                    '#3D4A8C', '#3E4B8F', '#3F4C92', '#404D95',  # Muted blue-purples
                    '#414E98', '#424F9B', '#43509E', '#4451A1'   # Dark blue-purples
                ]
                color = colors[tile % len(colors)]
                
                # Create tile background
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#4a6a9e', width=3)
                
                # Add inner highlight
                self.canvas.create_rectangle(x1+4, y1+4, x2-4, y2-4, outline='#6a8abe', width=1)
                
                # Calculate font size
                font_size = max(18, int(tile_size * 0.4))
                
                # Draw the number in bold white
                self.canvas.create_text(x1 + tile_size/2, y1 + tile_size/2, 
                                       text=str(tile), 
                                       font=("Arial", font_size, "bold"),
                                       fill='white',
                                       anchor='center')
                
        # Bind canvas click for tile detection
        self.canvas.bind("<Button-1>", self.on_canvas_click)
    
    def on_canvas_click(self, event):
        """Detect which tile was clicked"""
        # Get click coordinates
        x = event.x
        y = event.y
        
        # Get canvas dimensions
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width <= 1 or canvas_height <= 1:
            return
        
        size = SIZE
        tile_size = min(canvas_width, canvas_height) // size
        
        # Calculate offset
        total_width = tile_size * size
        total_height = tile_size * size
        offset_x = (canvas_width - total_width) // 2
        offset_y = (canvas_height - total_height) // 2
        
        # Check if click is within board
        if x < offset_x or x > offset_x + total_width or y < offset_y or y > offset_y + total_height:
            return
        
        # Calculate which tile was clicked
        col = (x - offset_x) // tile_size
        row = (y - offset_y) // tile_size
        tile_index = row * size + col
        tile_number = self.board.tiles[tile_index]
        
        # Move the tile if it's not blank
        if tile_number != 0:
            self.move_tile(tile_number)
    
    def move_tile(self, tile_num):
        if self.board.move_tile(tile_num):
            self.move_counter += 1
            self.draw_board()
            self.update_info()
            if self.board.is_solved():
                self.status_indicator.config(text="★ SOLVED! ★", fg='#00ff88')
                messagebox.showinfo("🎉 Puzzle Solved!", 
                                   f"Congratulations! You solved the puzzle in {self.move_counter} moves!")
    
    def update_info(self):
        self.moves_value.config(text=str(self.move_counter))
    
    def solve(self, algorithm):
        self.status_indicator.config(text="● Solving...", fg='#ffaa44')
        self.window.update()
        
        board_copy = self.board.copy()
        limit_reached = False
        nodes = 0
        
        if algorithm == 'bfs':
            moves, nodes, t, limit_reached = Solver.bfs(board_copy)
        elif algorithm == 'dfs':
            moves, nodes, t, limit_reached = Solver.dfs_limited(board_copy, DEPTH_LIMIT_DFS)
        elif algorithm == 'a_star_h1':
            moves, nodes, t = Solver.a_star(board_copy, heuristic_misplaced)
        elif algorithm == 'a_star_h2':
            moves, nodes, t = Solver.a_star(board_copy, heuristic_manhattan)
        else:
            return
        
        if moves is None:
            if limit_reached:
                self.status_indicator.config(text="● Limit reached", fg='#ff4444')
                node_limit = NODE_LIMIT_BFS if algorithm == 'bfs' else NODE_LIMIT_DFS
                messagebox.showinfo("Result", f"❌ Goal not achieved by {algorithm.upper()} algorithm after visiting {nodes} nodes.\n\nNode limit: {node_limit}\nTry using A* algorithms for this puzzle size.")
            else:
                self.status_indicator.config(text="● No solution found", fg='#ff4444')
                messagebox.showinfo("Result", f"❌ No solution found. DFS may need higher depth limit.")
            return
        
        self._animate_solution(moves)
        self.status_indicator.config(text="● Solved!", fg='#00ff88')
        messagebox.showinfo("Solution found", 
                           f"✅ Puzzle solved!\n\nMoves: {len(moves)}\nNodes expanded: {nodes}\nTime: {t:.4f}s")
    
    def _animate_solution(self, moves):
        for tile in moves:
            self.board.move_tile(tile)
            self.move_counter += 1
            self.draw_board()
            self.update_info()
            self.window.update()
            time.sleep(0.2)
    
    def compare_all(self):
        if self.board.is_solved():
            messagebox.showinfo("Info", "Board already solved. Please shuffle first.")
            return
        
        self.status_indicator.config(text="● Comparing algorithms...", fg='#ffaa44')
        self.window.config(cursor="watch")
        self.window.update()
        
        results = compare_algorithms(self.board)
        
        self.window.config(cursor="")
        self.status_indicator.config(text="● Comparison ready", fg='#4a9eff')
        
        result_str = "🔍 ALGORITHM COMPARISON (4x4 Puzzle)\n" + "="*50 + "\n\n"
        for algo, data in results.items():
            if data['moves'] is not None:
                result_str += f"📌 {algo}:\n"
                result_str += f"   → Solution length: {data['length']} moves\n"
                result_str += f"   → Nodes expanded: {data['nodes']}\n"
                result_str += f"   → Time taken: {data['time']:.4f} seconds\n\n"
            else:
                if data.get('limit_reached', False):
                    result_str += f"❌ {algo}: Goal not achieved after visiting {data['nodes']} nodes (node limit reached).\n\n"
                else:
                    result_str += f"❌ {algo}: No solution found within limits.\n\n"
        
        top = tk.Toplevel(self.window)
        top.title("Comparison Results")
        top.configure(bg='#0a0a1a')
        top.geometry("550x450")
        
        text_area = scrolledtext.ScrolledText(top, width=60, height=20, 
                                              bg='#1a1a2e', fg='#e0e0e0',
                                              font=("Courier New", 10),
                                              insertbackground='white',
                                              relief=tk.FLAT, bd=0)
        text_area.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)
        text_area.insert(tk.INSERT, result_str)
        text_area.configure(state='disabled')


# =============================================================================
# Main Execution
# =============================================================================
if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='#0a0a1a')
    app = PuzzleGUI(root)
    root.mainloop()