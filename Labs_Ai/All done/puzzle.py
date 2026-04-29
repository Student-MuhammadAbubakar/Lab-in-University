# =============================================================================
# SECTION A: Imports & Constants
# =============================================================================
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import heapq
import time
from collections import deque
from abc import ABC, abstractmethod

# Board size options
SIZES = [3, 4, 5]
DEFAULT_SIZE = 3
DEPTH_LIMIT_DFS = {3: 30, 4: 50, 5: 50}
GOAL_STATE = lambda size: list(range(1, size*size)) + [0]  # 0 represents the blank tile


# =============================================================================
# SECTION B: Puzzle Board Logic
# =============================================================================
class PuzzleBoard:
    """Represents the 15‑puzzle board and its operations."""
    
    def __init__(self, size):
        self.size = size
        self.tiles = GOAL_STATE(size)          # start solved
        self.blank_pos = len(self.tiles) - 1   # last position (0)
    
    def copy(self):
        """Return a deep copy of the board."""
        new_board = PuzzleBoard(self.size)
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
        """Check if the current arrangement is solvable."""
        inv = self.get_inversions()
        if self.size % 2 == 1:          # odd size
            return inv % 2 == 0
        else:                            # even size
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
        self.tiles = GOAL_STATE(self.size)
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
        return self.tiles == GOAL_STATE(self.size)


# =============================================================================
# SECTION C: Search Algorithms (BFS, DFS, A*)
# =============================================================================
class Solver:
    """Collection of static methods for solving the puzzle."""
    
    @staticmethod
    def bfs(initial_board):
        """Breadth‑First Search. Returns (moves_list, nodes_expanded, elapsed_time)."""
        start_time = time.time()
        queue = deque()
        queue.append((initial_board.copy(), []))   # (board, path_of_moves)
        visited = set()
        visited.add(tuple(initial_board.tiles))
        nodes_expanded = 0
        
        while queue:
            board, path = queue.popleft()
            nodes_expanded += 1
            
            if board.is_solved():
                elapsed = time.time() - start_time
                return path, nodes_expanded, elapsed
            
            for tile, neighbor in board.get_neighbors():
                state = tuple(neighbor.tiles)
                if state not in visited:
                    visited.add(state)
                    queue.append((neighbor, path + [tile]))
        
        elapsed = time.time() - start_time
        return None, nodes_expanded, elapsed   # no solution (should not happen for solvable puzzle)
    
    @staticmethod
    def dfs_limited(initial_board, depth_limit):
        """Depth‑limited DFS using recursion. Returns (moves, nodes_expanded, elapsed)."""
        start_time = time.time()
        visited = set()
        visited.add(tuple(initial_board.tiles))
        nodes_expanded = 0
        
        def dfs(board, path, depth):
            nonlocal nodes_expanded
            nodes_expanded += 1
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
            return None
        
        result = dfs(initial_board, [], 0)
        elapsed = time.time() - start_time
        return result, nodes_expanded, elapsed
    
    @staticmethod
    def a_star(initial_board, heuristic_func):
        """A* search. heuristic_func(board) returns h-value."""
        start_time = time.time()
        counter = 0                   # tie‑breaker for priority queue
        open_list = []
        # Each entry: (f, counter, g, board, path)
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
    goal = GOAL_STATE(board.size)
    return sum(1 for i, t in enumerate(board.tiles) if t != 0 and t != goal[i])

def heuristic_manhattan(board):
    """h₂: sum of Manhattan distances for each tile to its goal position."""
    size = board.size
    distance = 0
    for i, tile in enumerate(board.tiles):
        if tile == 0:
            continue
        # goal position of this tile
        goal_idx = tile - 1   # tiles are 1..size*size-1, 0 at end
        goal_row, goal_col = divmod(goal_idx, size)
        curr_row, curr_col = divmod(i, size)
        distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance


# =============================================================================
# SECTION D: Algorithm Comparison Runner
# =============================================================================
def compare_algorithms(board):
    """Run all solvers on a copy of the board and return a dictionary of results."""
    results = {}
    print("Running BFS...")
    moves, nodes, t = Solver.bfs(board.copy())
    results["BFS"] = {"moves": moves, "nodes": nodes, "time": t, "length": len(moves) if moves else None}
    
    print("Running DFS (depth-limited)...")
    depth = DEPTH_LIMIT_DFS.get(board.size, 50)
    moves, nodes, t = Solver.dfs_limited(board.copy(), depth)
    results["DFS"] = {"moves": moves, "nodes": nodes, "time": t, "length": len(moves) if moves else None}
    
    print("Running A* (h1 = Misplaced)...")
    moves, nodes, t = Solver.a_star(board.copy(), heuristic_misplaced)
    results["A* (h1)"] = {"moves": moves, "nodes": nodes, "time": t, "length": len(moves) if moves else None}
    
    print("Running A* (h2 = Manhattan)...")
    moves, nodes, t = Solver.a_star(board.copy(), heuristic_manhattan)
    results["A* (h2)"] = {"moves": moves, "nodes": nodes, "time": t, "length": len(moves) if moves else None}
    
    return results


# =============================================================================
# SECTION E: Tic‑Tac‑Toe Logic with Minimax
# =============================================================================
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'   # human
        self.ai_player = 'O'
        self.game_over = False
    
    def reset(self):
        self.__init__()
    
    def make_move(self, row, col):
        """Place mark and update turn. Returns True if valid."""
        if self.board[row][col] == ' ' and not self.game_over:
            self.board[row][col] = self.current_player
            if self.check_win(self.current_player):
                self.game_over = True
                return 'win'
            elif self.is_board_full():
                self.game_over = True
                return 'draw'
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return 'continue'
        return 'invalid'
    
    def check_win(self, player):
        b = self.board
        for i in range(3):
            if all(b[i][j] == player for j in range(3)): return True
            if all(b[j][i] == player for j in range(3)): return True
        if b[0][0] == player and b[1][1] == player and b[2][2] == player: return True
        if b[0][2] == player and b[1][1] == player and b[2][0] == player: return True
        return False
    
    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
    
    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
    
    def minimax(self, is_maximizing):
        """Minimax algorithm."""
        # Check terminal states
        if self.check_win(self.ai_player):
            return 10, None
        if self.check_win('X'):  # human
            return -10, None
        if self.is_board_full():
            return 0, None
        
        if is_maximizing:
            best_score = -float('inf')
            best_move = None
            for move in self.get_available_moves():
                self.board[move[0]][move[1]] = self.ai_player
                score, _ = self.minimax(False)
                self.board[move[0]][move[1]] = ' '
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for move in self.get_available_moves():
                self.board[move[0]][move[1]] = 'X'
                score, _ = self.minimax(True)
                self.board[move[0]][move[1]] = ' '
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move
    
    def ai_move(self):
        """Make AI move using Minimax."""
        if not self.game_over and self.current_player == self.ai_player:
            _, move = self.minimax(True)
            if move:
                self.board[move[0]][move[1]] = self.ai_player
                if self.check_win(self.ai_player):
                    self.game_over = True
                    return 'ai_win'
                elif self.is_board_full():
                    self.game_over = True
                    return 'draw'
                self.current_player = 'X'
                return 'ai_moved'
        return None


# =============================================================================
# SECTION F: GUI - Main Menu
# =============================================================================
class MainMenu:
    def __init__(self, root):
        self.root = root
        root.title("AI Games - Assignment")
        root.geometry("300x200")
        frame = ttk.Frame(root, padding=20)
        frame.pack(expand=True)
        
        ttk.Label(frame, text="Choose a Game", font=("Arial", 14)).pack(pady=10)
        ttk.Button(frame, text="15-Puzzle", command=self.open_puzzle).pack(pady=5, fill='x')
        ttk.Button(frame, text="Tic Tac Toe", command=self.open_tic_tac_toe).pack(pady=5, fill='x')
    
    def open_puzzle(self):
        self.new_window = tk.Toplevel(self.root)
        PuzzleGUI(self.new_window)
    
    def open_tic_tac_toe(self):
        self.new_window = tk.Toplevel(self.root)
        TicTacToeGUI(self.new_window)


# =============================================================================
# SECTION G: GUI - 15-Puzzle Window
# =============================================================================
class PuzzleGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("15-Puzzle Solver")
        self.size = DEFAULT_SIZE
        self.board = PuzzleBoard(self.size)
        self.board.shuffle(100)
        self.move_counter = 0
        
        # UI elements
        top_frame = ttk.Frame(window)
        top_frame.pack(pady=5)
        
        ttk.Label(top_frame, text="Size:").grid(row=0, column=0, padx=5)
        self.size_var = tk.IntVar(value=self.size)
        size_menu = ttk.OptionMenu(top_frame, self.size_var, self.size, *SIZES, command=self.change_size)
        size_menu.grid(row=0, column=1, padx=5)
        
        ttk.Button(top_frame, text="Shuffle", command=self.shuffle_board).grid(row=0, column=2, padx=5)
        ttk.Button(top_frame, text="Solve (BFS)", command=lambda: self.solve('bfs')).grid(row=0, column=3, padx=2)
        ttk.Button(top_frame, text="Solve (DFS)", command=lambda: self.solve('dfs')).grid(row=0, column=4, padx=2)
        ttk.Button(top_frame, text="Solve A* (h1)", command=lambda: self.solve('a_star_h1')).grid(row=0, column=5, padx=2)
        ttk.Button(top_frame, text="Solve A* (h2)", command=lambda: self.solve('a_star_h2')).grid(row=0, column=6, padx=2)
        ttk.Button(top_frame, text="Compare All", command=self.compare_all).grid(row=0, column=7, padx=5)
        
        # Canvas for puzzle board
        self.canvas = tk.Canvas(window, width=300, height=300, bg='white')
        self.canvas.pack(pady=10)
        
        self.info_label = ttk.Label(window, text="Moves: 0")
        self.info_label.pack()
        
        self.draw_board()
    
    def change_size(self, new_size):
        self.size = int(new_size)
        self.board = PuzzleBoard(self.size)
        self.board.shuffle(100)
        self.move_counter = 0
        self.update_info()
        self.draw_board()
    
    def shuffle_board(self):
        self.board.shuffle(100)
        self.move_counter = 0
        self.update_info()
        self.draw_board()
    
    def draw_board(self):
        self.canvas.delete("all")
        size = self.size
        tile_w = 300 // size
        tile_h = 300 // size
        for i, tile in enumerate(self.board.tiles):
            if tile == 0:
                continue
            row, col = divmod(i, size)
            x1 = col * tile_w
            y1 = row * tile_h
            x2 = x1 + tile_w
            y2 = y1 + tile_h
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black")
            self.canvas.create_text(x1 + tile_w/2, y1 + tile_h/2, text=str(tile), font=("Arial", 16))
            self.canvas.tag_bind(self.canvas.find_all()[-2], "<Button-1>", lambda e, t=tile: self.move_tile(t))
    
    def move_tile(self, tile_num):
        if self.board.move_tile(tile_num):
            self.move_counter += 1
            self.draw_board()
            self.update_info()
            if self.board.is_solved():
                messagebox.showinfo("Solved!", f"You solved the puzzle in {self.move_counter} moves!")
    
    def update_info(self):
        self.info_label.config(text=f"Moves: {self.move_counter}")
    
    def solve(self, algorithm):
        """Solve and animate solution."""
        board_copy = self.board.copy()
        if algorithm == 'bfs':
            moves, nodes, t = Solver.bfs(board_copy)
        elif algorithm == 'dfs':
            moves, nodes, t = Solver.dfs_limited(board_copy, DEPTH_LIMIT_DFS.get(self.size, 50))
        elif algorithm == 'a_star_h1':
            moves, nodes, t = Solver.a_star(board_copy, heuristic_misplaced)
        elif algorithm == 'a_star_h2':
            moves, nodes, t = Solver.a_star(board_copy, heuristic_manhattan)
        else:
            return
        
        if moves is None:
            messagebox.showinfo("Result", "No solution found (DFS may need higher depth limit)")
            return
        
        # Animate solution step by step
        self._animate_solution(moves)
        messagebox.showinfo("Solution found", f"Moves: {len(moves)}\nNodes expanded: {nodes}\nTime: {t:.4f}s")
    
    def _animate_solution(self, moves):
        """Animate solution by moving tiles one by one."""
        for tile in moves:
            self.board.move_tile(tile)
            self.move_counter += 1
            self.draw_board()
            self.window.update()
            time.sleep(0.3)
    
    def compare_all(self):
        """Run all algorithms and display comparison."""
        if self.board.is_solved():
            messagebox.showinfo("Info", "Board already solved. Please shuffle first.")
            return
        
        # Disable button during computation
        self.window.config(cursor="watch")
        self.window.update()
        
        results = compare_algorithms(self.board)
        
        self.window.config(cursor="")
        
        # Build result string
        result_str = "Algorithm Comparison (same starting board)\n\n"
        for algo, data in results.items():
            if data['moves'] is not None:
                result_str += f"{algo}: Length={data['length']}, Nodes={data['nodes']}, Time={data['time']:.4f}s\n"
            else:
                result_str += f"{algo}: No solution found within limits.\n"
        
        # Show in a new window with scrollable text
        top = tk.Toplevel(self.window)
        top.title("Comparison Results")
        text_area = scrolledtext.ScrolledText(top, width=60, height=15)
        text_area.pack(padx=10, pady=10)
        text_area.insert(tk.INSERT, result_str)
        text_area.configure(state='disabled')


# =============================================================================
# SECTION H: GUI - Tic‑Tac‑Toe Window
# =============================================================================
class TicTacToeGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic Tac Toe - Minimax")
        self.game = TicTacToe()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.status_label = ttk.Label(window, text="Your turn (X)", font=("Arial", 12))
        self.status_label.pack(pady=5)
        
        board_frame = ttk.Frame(window)
        board_frame.pack()
        for i in range(3):
            for j in range(3):
                btn = tk.Button(board_frame, text=' ', font=("Arial", 20), width=5, height=2,
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j] = btn
        
        ttk.Button(window, text="Restart", command=self.restart).pack(pady=10)
    
    def restart(self):
        self.game.reset()
        self.update_board()
        self.status_label.config(text="Your turn (X)")
    
    def on_click(self, row, col):
        if self.game.current_player != 'X' or self.game.game_over:
            return
        result = self.game.make_move(row, col)
        self.update_board()
        if result == 'win':
            self.status_label.config(text="You win!")
            messagebox.showinfo("Game Over", "You win!")
        elif result == 'draw':
            self.status_label.config(text="Draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            # AI moves
            self.status_label.config(text="AI thinking...")
            self.window.update()
            ai_result = self.game.ai_move()
            self.update_board()
            if ai_result == 'ai_win':
                self.status_label.config(text="AI wins!")
                messagebox.showinfo("Game Over", "AI wins!")
            elif ai_result == 'draw':
                self.status_label.config(text="Draw!")
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.status_label.config(text="Your turn (X)")
    
    def update_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=self.game.board[i][j])


# =============================================================================
# SECTION I: Main Execution
# =============================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()