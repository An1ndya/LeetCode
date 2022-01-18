func searchMatrix(matrix [][]int, target int) bool {
    m:=len(matrix)
    n:=len(matrix[0])
    
    //row wise
    l:=0 
    r:=m-1
    row:=0
    for l <= r {
        middle:= int((l+r)/2)
        
        if matrix[middle][0] == target{
            return true
        }
        
        if target < matrix[middle][0]{
            r = middle - 1 
        }else{
            l = middle + 1
        }
        row = middle
    }  
    //fmt.Println(row)
    
    if matrix[row][0] > target && row != 0 {row--}
    
    //inside the row 
    l=0 
    r=n-1
    
    for l <= r {
        middle:= int((l+r)/2)
        
        if matrix[row][middle] == target{
            return true
        }
        
        if target < matrix[row][middle]{
            r = middle - 1 
        }else{
            l = middle + 1
        }
    }
    return false
}