def find_blank(puzzle):
   return puzzle.index('0')
def swap(puzzle, pos1, pos2):
    puzzle_list = list(puzzle)
    puzzle_list[pos1],puzzle_list[pos2] = puzzle_list[pos2],puzzle_list[pos1]
    return ''.join(puzzle_list)
def move_up(puzzle):
    blank = find_blank(puzzle)
    if blank >= 3:
        return swap(puzzle, blank, blank - 3)
    else:
        return None
def move_down(puzzle):
    blank = find_blank(puzzle)
    if blank <= 5:
        return swap(puzzle, blank, blank + 3)
    else:
        return None


def move_left(puzzle):
    blank = find_blank(puzzle)
    if blank % 3 != 0:
        return swap(puzzle, blank, blank - 1)
    else:
        return None


def move_right(puzzle):
    blank = find_blank(puzzle)
    if blank % 3 != 2:
        return swap(puzzle, blank, blank + 1)
    else:
        return None


def get_all_moves(puzzle):
    all_moves = []
    
    result = move_up(puzzle)
    if result is not None:
        all_moves.append(result)
    
    result = move_down(puzzle)
    if result is not None:
        all_moves.append(result)
    
    result = move_left(puzzle)
    if result is not None:
        all_moves.append(result)
    
    result = move_right(puzzle)
    if result is not None:
        all_moves.append(result)
    
    return all_moves
def calculate_distance(puzzle, goal="123456780"):
    total_distance = 0
    
    position = 0
    while position < 9:
        tile = puzzle[position]
        
        if tile != '0':
            current_row = position // 3
            current_col = position % 3
            
            goal_position = 0
            while goal_position < 9:
                if goal[goal_position] == tile:
                    break
                goal_position = goal_position + 1
            
            goal_row = goal_position // 3
            goal_col = goal_position % 3
            
            row_distance = current_row - goal_row
            if row_distance < 0:
                row_distance = -row_distance
            
            col_distance = current_col - goal_col
            if col_distance < 0:
                col_distance = -col_distance
            
            total_distance = total_distance + row_distance + col_distance
        
        position = position + 1
    
    return total_distance


def print_puzzle(puzzle):
    print(puzzle[0], puzzle[1], puzzle[2])
    print(puzzle[3], puzzle[4], puzzle[5])
    print(puzzle[6], puzzle[7], puzzle[8])
    print()


def solve_puzzle(start, goal="123456780"):
    
    if start == goal:
        return [start]
    
    todo_list = []
    start_distance = calculate_distance(start, goal)
    todo_list.append([start_distance, start, [start], 0])
    
    seen = {}
    seen[start] = 0
    
    while len(todo_list) > 0:
        
        best_index = 0
        i = 0
        while i < len(todo_list):
            if todo_list[i][0] < todo_list[best_index][0]:
                best_index = i
            i = i + 1
        
        current_item = todo_list[best_index]
        del todo_list[best_index]
        
        f_score = current_item[0]
        current_puzzle = current_item[1]
        path_so_far = current_item[2]
        moves_made = current_item[3]
        
        if current_puzzle == goal:
            return path_so_far
        
        next_puzzles = get_all_moves(current_puzzle)
        
        next_index = 0
        while next_index < len(next_puzzles):
            next_puzzle = next_puzzles[next_index]
            
            new_moves = moves_made + 1
            
            should_explore = False
            
            if next_puzzle not in seen:
                        should_explore = True
            elif new_moves < seen[next_puzzle]:
                should_explore = True
            
            if should_explore:
                seen[next_puzzle] = new_moves
                new_distance = calculate_distance(next_puzzle, goal)
                new_f_score = new_moves + new_distance
                new_path = path_so_far + [next_puzzle]
                todo_list.append([new_f_score, next_puzzle, new_path, new_moves])
            
            next_index = next_index + 1
    
    return None


start_puzzle = "123456708"

print("=" * 50)
print("STARTING PUZZLE:")
print("=" * 50)
print_puzzle(start_puzzle)

print("GOAL PUZZLE:")
print_puzzle("123456780")

print("SOLVING... Please wait...")
print()

solution = solve_puzzle(start_puzzle)

if solution != None:
    number_of_moves = len(solution) - 1
    print("=" * 50)
    print("SOLUTION FOUND!")
    print("=" * 50)
    print("Number of moves needed:", number_of_moves)
    print()
    
    step_number = 0
    while step_number < len(solution):
        print("STEP", step_number, ":")
        print_puzzle(solution[step_number])
        step_number = step_number + 1
else:
    print("No solution found!")