function findKthLargest(nums: number[], k: number): number 
{
    nums.sort(function(a, b){return b - a});
    return nums[k-1];

};