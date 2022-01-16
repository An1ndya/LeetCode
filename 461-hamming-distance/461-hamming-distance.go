func hammingDistance(x int, y int) int {
    
    xor := x ^ y
    return hammingWeight(xor)
}
func hammingWeight(num int) int {

    weight:=0

    for i:=0;i<32;i++ {
        
        if num & 1 == 1{ weight++ }
        num = num >> 1
    }  
    return weight   
}