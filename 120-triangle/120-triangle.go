func minimumTotal(triangle [][]int) int {
    
    n:=len(triangle)

    for i :=n-2;i>=0;i--{
        for j:=i;j>=0;j--{
            triangle [i][j] += min(triangle [i+1][j],triangle [i+1][j+1]) 
        }
    }
    return triangle[0][0]
}
func min(a int, b int ) int{
    if a > b{
        return b
    }else{
        return a
    }
}