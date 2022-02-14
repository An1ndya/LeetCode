# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
    n=nums.length()
    mn=mp=ans=minp=maxp=nums[0]
    p=1

    for i in 1..n-1 do
        mp= [nums[i], maxp*nums[i], minp*nums[i]].max
        mn= [nums[i], maxp*nums[i], minp*nums[i]].min
        maxp=mp
        minp=mn
        ans=  [maxp,ans].max
    end
    return ans
end