func peakIndexInMountainArray(arr []int) int {
        
    n:=len(arr)
    l:=0 
    r:=n-1
    
    for l <= r {
        
        //fmt.Println(l, " ",r)
  
        m:= int((l+r)/2)
        
        if m > 0 && m < n-1 && arr[m] > arr[m-1] && arr[m] > arr[m+1]  { return m}
              
        if arr[m] < arr[m+1] {
            l = m + 1
        }else{
            r = m -1
        }
    }
    return 0
}