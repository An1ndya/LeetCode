func minimumArea(grid [][]int) int {
    m := len(grid)
    if m == 0 {
        return 0
    }
    n := len(grid[0])

    minRow, minCol := m, n
    maxRow, maxCol := -1, -1

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                if i < minRow {
                    minRow = i
                }
                if i > maxRow {
                    maxRow = i
                }
                if j < minCol {
                    minCol = j
                }
                if j > maxCol {
                    maxCol = j
                }
            }
        }
    }

    if maxRow == -1 {
        // no '1' in grid
        return 0
    }

    return (maxRow - minRow + 1) * (maxCol - minCol + 1)
}