romania = {
    'sibiu':['Fagaras', 'rimnicu', 'Vilcea'],
    'Fagaras':['Bucharest'],
    'Rimnicu Vilcea':["Pitesti"],
    'Pitesti':['Bucharest'],
}

def breadth_first(start,goal,neighbors):
    frontier = [start]
    previous = {start: None}
    while frontier:
        current = frontier.pop(0)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = previous[current]
            return path[::-1]
        for neighbor in neighbors.get(current, []):
            if neighbor not in previous:
                previous[neighbor] = current
                frontier.append(neighbor)
    return None

def depth_first(start,goal,neighbors):
    frontier = [start]
    previous = {start: None}
    while frontier:
        current = frontier.pop()
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = previous[current]
            return path[::-1]
        for neighbor in neighbors.get(current, []):
            if neighbor not in previous:
                previous[neighbor] = current
                frontier.append(neighbor)
    return None


start_state = 'sibiu'
goal_state = 'Bucharest'

result_bfs = breadth_first(start_state, goal_state, romania)
result_dfs = depth_first(start_state, goal_state, romania)
print("Breadth-First Search Result:", result_bfs)
print("Depth-First Search Result:", result_dfs)