import random

def initial_state():
    return random.randint(10, 25)

def possible_new_states(state):
    new_state = []
    for take in (1, 2, 3):
        if take <= state:
            new_state.append(state - take)
    return new_state  # fixed indentation

def evaluate_state(state, is_maximizing):
    if state == 0:
        return -1 if is_maximizing else 1
    return None

def minimax(state, is_maximizing):
    score = evaluate_state(state, is_maximizing)
    if score is not None:
        return score
    moves = []
    for new_state in possible_new_states(state):
        result = minimax(new_state, not is_maximizing)
        moves.append(result)
    return max(moves) if is_maximizing else min(moves)

def best_move(state):
    # Find the best move for the AI (maximizing player)
    candidates = possible_new_states(state)
    return max(candidates, key=lambda s: minimax(s, is_maximizing=False))
    # Note: After AI moves, it becomes the player's turn, so the next call uses is_maximizing=False

def game_over(score):
    print("You win!" if score > 0 else "I win!")

def input_choice(state):
    while True:
        try:
            max_take = min(3, state)
            choice = int(input(f"How many coins do you want to take? (1-{max_take}) "))
            if 1 <= choice <= max_take:
                return choice
            else:
                print(f"Invalid choice. You can take 1 to {max_take} coins.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    state = initial_state()
    while True:
        print(f"\nCurrent coins: {state}")
        # Player's turn
        choice = input_choice(state)  # fixed: pass state, not moves
        state -= choice
        score = evaluate_state(state, is_maximizing=False)
        if score is not None:
            game_over(score)
            break

        # AI's turn
        ai_move = best_move(state)
        print(f"I take coins, leaving {ai_move}")
        state = ai_move
        score = evaluate_state(state, is_maximizing=True)
        if score is not None:
            game_over(score)
            break

if __name__ == "__main__":
    play_game()