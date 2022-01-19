/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * type MountainArray struct {
 * }
 *
 * func (this *MountainArray) get(index int) int {}
 * func (this *MountainArray) length() int {}
 */

func findInMountainArray(target int, mountainArr *MountainArray) int {
    
    n:=mountainArr.length()
    l:=0 
    r:=n-1
    peakindex:= 0
    
    //find peak
    for l <= r {
        
        //fmt.Println(l, " ",r)
  
        m:= int((l+r)/2)
        
        middle:= mountainArr.get(m)
        left:= 0
        right:= mountainArr.get(m+1)
        
        if m > 0 && m < n-1{
        
            left= mountainArr.get(m-1)
            
            if middle > left && middle > right { 
                if middle == target {return m}
                peakindex = m
                break
            }
        } 
              
        if middle < right {
            l = m + 1
        }else{
            r = m -1
        }
    }
    //find left side--if found will return minimum index
    l=0 
    r= peakindex - 1

    for l <= r {
        
        //fmt.Println(l, " ",r)
  
        m:= int((l+r)/2)
        
        middle:= mountainArr.get(m)

        if middle == target {return m} 
              
        if middle < target {
            l = m + 1
        }else{
            r = m -1
        }
    }
    //right side    
    l= peakindex + 1
    r= n-1

    for l <= r {
        
        //fmt.Println(l, " ",r)
  
        m:= int((l+r)/2)
        
        middle:= mountainArr.get(m)

        if middle == target {return m} 
              
        if middle > target {
            l = m + 1
        }else{
            r = m -1
        }
    }
    return -1
}