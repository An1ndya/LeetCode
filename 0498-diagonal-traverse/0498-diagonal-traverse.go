func findDiagonalOrder(mat [][]int) []int {
    if len(mat) == 0 || len(mat[0]) == 0 {
        return []int{}
    }

    m, n := len(mat), len(mat[0])
    res := make([]int, 0, m*n)
    row, col, direction := 0, 0, 1

    for len(res) < m*n {
        res = append(res, mat[row][col])

        if direction == 1 { // going up-right
            if col == n-1 {
                row++
                direction = -1
            } else if row == 0 {
                col++
                direction = -1
            } else {
                row--
                col++
            }
        } else { // going down-left
            if row == m-1 {
                col++
                direction = 1
            } else if col == 0 {
                row++
                direction = 1
            } else {
                row++
                col--
            }
        }
    }

    return res
}
