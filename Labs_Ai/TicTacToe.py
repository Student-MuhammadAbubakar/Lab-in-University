import tkinter as tk
def check_winner(board, player):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for line in wins:
        if all(board[i] == player for i in line):
            return True
    return False
def is_board_full(board):
    return all(cell != "" for cell in board)

def minimax(board, is_maximizing):

    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best = -100
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = ""
                if score > best:
                    best = score
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = ""
                if score < best:
                    best = score
        return best


def best_move(board):

    best_score = -100
    move = -1
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe – Minimax AI")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self.board = [""] * 9
        self.human = "X"
        self.ai = "O"
        self.game_over = False
        self.build_ui()

    def build_ui(self):

        tk.Label(
            self.root,
            text="Tic  Tac  Toe",
            font=("Arial", 22, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4",
        ).pack(pady=12)

        tk.Label(
            self.root,
            text="You are X   |   AI is O",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#a6e3a1",
        ).pack()
        grid_frame = tk.Frame(self.root, bg="#1e1e2e")
        grid_frame.pack(pady=15, padx=20)

        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                grid_frame,
                text="",
                width=5,
                height=2,
                font=("Arial", 28, "bold"),
                bg="#313244",
                fg="#cdd6f4",
                activebackground="#45475a",
                relief="flat",
                bd=0,
                command=lambda idx=i: self.human_move(idx),
            )
            btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)
            self.buttons.append(btn)

        self.status = tk.StringVar(value="Your turn! Click a cell.")
        tk.Label(
            self.root,
            textvariable=self.status,
            font=("Arial", 13),
            bg="#1e1e2e",
            fg="#f5c2e7",
        ).pack(pady=6)

        tk.Button(
            self.root,
            text="Restart",
            font=("Arial", 12, "bold"),
            bg="#89b4fa",
            fg="#1e1e2e",
            padx=16,
            pady=6,
            relief="flat",
            command=self.restart,
        ).pack(pady=10)

    def human_move(self, idx):
        if self.game_over or self.board[idx] != "":
            return

        self.board[idx] = self.human
        self.buttons[idx].config(text="X", fg="#f38ba8")

        if check_winner(self.board, self.human):
            self.status.set("🎉 You win!  (That was lucky…)")
            self.highlight_winner(self.human)
            self.game_over = True
            return

        if is_board_full(self.board):
            self.status.set("It's a draw!")
            self.game_over = True
            return

        self.status.set("AI is thinking…")
        self.root.update()
        self.root.after(300, self.ai_move)

    def ai_move(self):
        move = best_move(self.board)
        if move == -1:
            return

        self.board[move] = self.ai
        self.buttons[move].config(text="O", fg="#a6e3a1")

        if check_winner(self.board, self.ai):
            self.status.set("😈 AI wins!  Better luck next time.")
            self.highlight_winner(self.ai)
            self.game_over = True
            return

        if is_board_full(self.board):
            self.status.set("It's a draw!")
            self.game_over = True
            return

        self.status.set("Your turn! Click a cell.")

    def highlight_winner(self, player):
        wins = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for line in wins:
            if all(self.board[i] == player for i in line):
                for i in line:
                    self.buttons[i].config(bg="#f9e2af")
                break

    def restart(self):
        self.board = [""] * 9
        self.game_over = False
        for btn in self.buttons:
            btn.config(text="", bg="#313244")
        self.status.set("Your turn! Click a cell.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
