# @param {Integer[]} nums
# @return {Integer}
def get_max_len(nums)
    n=nums.length()
    maxnegativei=0
    minnegativei=100000
    countnegtive=0
    ans=0
    start=0
    for i in 0..n-1 do

        if nums[i] < 0
            countnegtive+=1
            if i > maxnegativei; maxnegativei = i end
            if i < minnegativei; minnegativei = i end
        end   
        if countnegtive % 2 ==0
            if nums[i] != 0 ; ans=[ans,i-start+1].max
            else ans=[ans,i-start].max
            end
        elsif countnegtive > 0
            if nums[i] != 0
                ans=[ans,i-minnegativei, maxnegativei-start].max
                #puts i,minnegativei, maxnegativei,ans
            end
        end
        if nums[i] == 0
            maxnegativei=0
            minnegativei=100000
            countnegtive=0
            start=i+1        
        end
    end
        
    return ans
end