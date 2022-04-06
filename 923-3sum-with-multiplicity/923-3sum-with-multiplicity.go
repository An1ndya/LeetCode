func threeSumMulti(arr []int, target int) int {
    ///triplets := [][]int{}
    sort.Ints(arr)
    n:= len(arr)
    ans:=0

    for i:=0;i<n;i++{
        
        if arr[i] > target {continue}
        
        left, right := i+1, n-1
        
        for left < right{
    
            sum := arr[i] + arr[left] + arr[right]
            
            if sum == target {
                if arr[left] != arr[right]{
                    countleft:=1
                    countright:=1
                    for left < right && arr[left]==arr[left+1] {
                        left++
                        countleft++
                    }
                    for left < right && arr[right]==arr[right-1] {
                        right--
                        countright++
                    }
                    //fmt.Println(, countleft, countright )
                    ans+=countleft*countright
                    ans%= 1000000007
                    //need point to next no equal value
                    left++
                    right--
                }else{
                    count:=right-left+1
                    ans+=count*(count-1)/2
                    ans%= 1000000007
                    break;
                }
                  
            }else if sum > target {
                right--   
            }else {     //sum < target
                left++
            }
        }
    }
    //fmt.Print(triplets)
    return ans
}