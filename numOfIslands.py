# numOfIslands.py
# Problem 1: Number of Islands
# This file contains both DFS and BFS implementations to solve the number of islands problem.
# Each part is labeled and commented with explanations and complexity analysis.

from typing import List
from collections import deque

# ------------------------------
# Helper Function for Grid Boundaries
# ------------------------------
def is_valid(r: int, c: int, grid: List[List[str]]) -> bool:
    """Check if (r, c) is within bounds and is land ('1')."""
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1'

# ------------------------------
# PART 1: DFS Implementation
# ------------------------------
def num_islands_dfs(grid: List[List[str]]) -> int:
    """
    Count the number of islands using Depth-First Search (DFS).

    Args:
        grid: 2D list representing the map ('1' for land, '0' for water)

    Returns:
        Number of islands
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r: int, c: int):
        """Recursive DFS to mark all connected land."""
        if not is_valid(r, c, grid) or visited[r][c]:
            return
        visited[r][c] = True
        # Explore all 4 directions (no diagonals)
        dfs(r - 1, c)  # up
        dfs(r + 1, c)  # down
        dfs(r, c - 1)  # left
        dfs(r, c + 1)  # right

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not visited[r][c]:
                dfs(r, c)
                count += 1  # Found one island

    return count

# ------------------------------
# PART 2: BFS Implementation
# ------------------------------
def num_islands_bfs(grid: List[List[str]]) -> int:
    """
    Count the number of islands using Breadth-First Search (BFS).

    Args:
        grid: 2D list representing the map ('1' for land, '0' for water)

    Returns:
        Number of islands
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def bfs(r: int, c: int):
        """Use a queue to explore connected land iteratively."""
        queue = deque()
        queue.append((r, c))
        visited[r][c] = True

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = row + dr, col + dc
                if is_valid(nr, nc, grid) and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not visited[r][c]:
                bfs(r, c)
                count += 1  # Found one island

    return count

# ------------------------------
# Complexity Analysis
# ------------------------------
"""
Time Complexity (both DFS and BFS): O(m * n)
  - Each cell is visited once and only once.

Space Complexity:
  - DFS: O(m * n) in worst case for recursion stack and visited matrix.
  - BFS: O(m * n) in worst case for queue and visited matrix.

m = number of rows
n = number of columns
"""

# ------------------------------
# Method Comparison
# ------------------------------
"""
DFS vs BFS - Which is better?

In this problem, both DFS and BFS are equally valid. However:

- DFS is typically easier to write recursively.
- BFS uses a queue and may be slightly more memory-intensive.
- DFS can cause stack overflow on very large grids unless you use an iterative version.

➡ For smaller grids, DFS is usually faster to implement.
➡ For larger grids, BFS is often more robust if implemented iteratively.

Conclusion: DFS is simpler; BFS is safer for large grids.
"""

# ------------------------------
# Test Case for Both Methods
# ------------------------------
if __name__ == "__main__":
    test_grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print("DFS - Number of Islands:", num_islands_dfs([row[:] for row in test_grid]))  # Deep copy for fresh grid
    print("BFS - Number of Islands:", num_islands_bfs([row[:] for row in test_grid]))
