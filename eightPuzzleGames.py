# eightPuzzleGames.py
# Problem 2: 8 Puzzle Game using A* Search Algorithm with Manhattan Distance
# This file solves the classic 8-puzzle sliding game using informed search.
# Explanations and complexity analysis are included in comments.

import heapq

# ------------------------------
# Puzzle Configuration
# ------------------------------
# Each puzzle state is represented as a flat list of length 9, e.g.:
# [1, 2, 3, 4, 5, 6, 7, 8, 0]
# where 0 represents the blank tile

# Goal configuration
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Directions for moving the blank tile (row, col): up, down, left, right
MOVES = {
    'U': -3,
    'D': 3,
    'L': -1,
    'R': 1
}

# ------------------------------
# Manhattan Distance Heuristic
# ------------------------------
def manhattan_distance(state):
    """Calculate the Manhattan distance for a given puzzle state."""
    distance = 0
    for i, val in enumerate(state):
        if val == 0:
            continue  # skip the blank tile
        goal_idx = GOAL_STATE.index(val)
        curr_row, curr_col = divmod(i, 3)
        goal_row, goal_col = divmod(goal_idx, 3)
        distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

# ------------------------------
# A* Search Algorithm
# ------------------------------
def a_star(start_state):
    """
    Perform A* search from start_state to GOAL_STATE using Manhattan distance.
    
    Returns:
        path (list): sequence of moves leading to the goal
        steps (int): number of steps taken
    """
    frontier = []
    heapq.heappush(frontier, (manhattan_distance(start_state), 0, start_state, []))  # (f = g + h, g, state, path)
    visited = set()

    while frontier:
        f, g, state, path = heapq.heappop(frontier)
        state_tuple = tuple(state)

        if state == GOAL_STATE:
            return path, g

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        zero_idx = state.index(0)
        row, col = divmod(zero_idx, 3)

        for move, delta in MOVES.items():
            new_idx = zero_idx + delta
            # Check if move is valid
            if move == 'L' and col == 0: continue
            if move == 'R' and col == 2: continue
            if move == 'U' and row == 0: continue
            if move == 'D' and row == 2: continue
            if not (0 <= new_idx < 9): continue

            # Generate new state
            new_state = state[:]
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            if tuple(new_state) not in visited:
                h = manhattan_distance(new_state)
                heapq.heappush(frontier, (g + 1 + h, g + 1, new_state, path + [move]))

    return None, -1  # No solution found

# ------------------------------
# Example Test Case
# ------------------------------
if __name__ == "__main__":
    # Example scrambled configuration (solvable)
    start = [1, 2, 3,
             4, 0, 6,
             7, 5, 8]

    path, steps = a_star(start)
    if path:
        print("Moves to solve:", path)
        print("Total steps:", steps)
    else:
        print("No solution found.")

# ------------------------------
# Complexity Analysis
# ------------------------------
"""
Time Complexity: 
    - In worst case, A* explores many permutations of the board: O(N!), where N = 9 (but pruning + heuristic reduces it).
    - In practice, it's much faster due to effective pruning by Manhattan distance.

Space Complexity:
    - Stores visited states and heap, up to O(N!) in worst case.
    - Practically smaller with a good heuristic.
"""

# ------------------------------
# Heuristic Explanation
# ------------------------------
"""
We use the Manhattan distance heuristic, which is admissible and consistent.
It calculates how far each tile is from its goal position, ignoring other tiles.
This ensures A* finds the optimal path and keeps the search efficient.
"""

