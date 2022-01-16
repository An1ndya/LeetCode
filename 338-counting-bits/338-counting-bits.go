func countBits(n int) []int {
    ans:=make([]int,n+1)
    for i:=0;i<=n;i++{
        ans[i] = hammingWeight(i)
    }
    return ans
}
func hammingWeight(num int) int {

    weight:=0

    for i:=0;i<32;i++ {
        
        if num & 1 == 1{ weight++ }
        num =num >> 1
    }
    
    return weight   
}
