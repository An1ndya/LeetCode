# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
    ans=0
    for n in nums
       ans^=n 
    end
    return ans
end