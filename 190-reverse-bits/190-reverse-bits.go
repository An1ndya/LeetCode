func reverseBits(num uint32) uint32 {
    var reverse uint32 = 0
    for i:=0;i<32;i++ {
        
        reverse = reverse | num & 1 
        if i < 31 {reverse = reverse << 1}
        num = num >> 1
    }  
    return reverse
}