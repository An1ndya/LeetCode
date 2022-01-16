func isPowerOfTwo(n int) bool {
    

    foundone := false
    
    if n < 1 { return false}

    for i:=0;i<32;i++ {
        
        if foundone == false{
            if n & 1 == 1{ foundone = true }
        }else{
            if n & 1 == 1 {return false}
        }
        n = n >> 1
    }
    
    return true
}
