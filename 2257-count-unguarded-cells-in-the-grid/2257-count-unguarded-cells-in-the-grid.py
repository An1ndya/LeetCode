class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid with 0 for unoccupied cells
        grid = [[0] * n for _ in range(m)]

        # Mark guards with 1 and walls with 2
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
        # Directions for north, south, east, west
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Mark guarded cells in the grid
        for gr, gc in guards:
            for dr, dc in directions:
                r, c = gr+dr, gc+dc
                while 0 <= r < m and 0 <= c < n:
                    if grid[r][c] in (1, 2):  # Stop at a guard or a wall
                        break
                    if grid[r][c] == 0:  # Mark as guarded
                        grid[r][c] = -1
                    r += dr
                    c += dc
        #print(grid)
        # Count unguarded cells
        unguarded_cells = sum(row.count(0) for row in grid)
        return unguarded_cells