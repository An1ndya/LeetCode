func searchMatrix(matrix [][]int, target int) bool {
    
    m:= len(matrix)
    n:= len(matrix[0])
    
    col:=0
    row:=m-1
    
    for row >=0 && col < n{
        value := matrix[row][col]
        
        if value == target {return true}
        
        if value > target{
            row--
        }else{
            col++
        }
    }
    return false
}