function runningSum(nums: number[]): number[] 
{
    let n= nums.length;
    let sm =0;
    for(let i=0;i<n;i++)
    {
        nums[i]+=sm;
        sm=nums[i];
    }
    return nums;
};