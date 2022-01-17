func findDifferentBinaryString(nums []string) string {

    var i,j,l int64
    n:= int64(len(nums))
    m:= make(map[int64]bool)
    for i=0;i<n;i++{
        intvalue, err := strconv.ParseInt(nums[i], 2, 64)
        if err == nil {m[intvalue] = true}
    }
    for i=0;i<20;i++{
        if m[i] == false{
            binarystring := strconv.FormatInt(i, 2)
            l = int64(len(binarystring))
            str := ""
            for j=0;j<n-l;j++ { str += "0" }
            str += binarystring
            return str
        }
        
    }
    return ""
}