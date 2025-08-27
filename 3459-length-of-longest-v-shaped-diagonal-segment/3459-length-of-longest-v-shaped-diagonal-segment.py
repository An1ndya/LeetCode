class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # Directions correspond to diagonals:
        # 0 → down-right (↘), 1 → down-left (↙), 
        # 2 → up-left (↖),   3 → up-right (↗)
        DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(cx: int, cy: int, direction: int, turn: bool, target: int) -> int:
            """
            Recursive DFS with memoization:
            cx, cy    → current position in the grid
            direction → current diagonal direction (0–3)
            turn      → whether we still have the option to turn (True/False)
            target    → what number we are expecting at the next cell (2, 0, 2, 0...)
            """

            # Next coordinates in the current direction
            nx, ny = cx + DIRS[direction][0], cy + DIRS[direction][1]

            # Base case: stop if out of bounds or next cell doesn't match the required target
            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != target:
                return 0

            # Continue in the same direction
            max_step = dfs(nx, ny, direction, turn, 2 - target)

            # If we still have a turn available, try turning clockwise (90°)
            if turn:
                # (direction + 1) % 4 ensures clockwise turn among diagonals
                max_step = max(
                    max_step,
                    dfs(nx, ny, (direction + 1) % 4, False, 2 - target),
                )

            # +1 because we successfully moved one step in the sequence
            return max_step + 1

        res = 0
        # Try starting from every cell in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # Only start from cells containing 1
                    for direction in range(4):  # Try all four diagonal directions
                        # Start DFS expecting the next value = 2
                        # We add +1 because starting cell (1) is part of the path
                        res = max(res, dfs(i, j, direction, True, 2) + 1)

        return res
