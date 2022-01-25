# @param {Integer[]} arr
# @return {Boolean}
def valid_mountain_array(arr)
    
    n = arr.length()
    isIncreasing = true
    i = 0
    if n < 3 then return false end
    if arr[0] > arr[1] then return false end
        
    for i in 1..n-1 do
        
        if arr[i] == arr[i-1] then return false end
            
        if isIncreasing
            if  arr[i] < arr[i-1] then isIncreasing = false end
        else
            if arr[i] > arr[i-1] then return false end
        end
        
    end
    if isIncreasing            
        return false
    else
        return true
    end
end