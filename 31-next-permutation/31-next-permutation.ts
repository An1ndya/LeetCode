/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void 
{
    let n= nums.length;
    let i=n-2;
    while(nums[i] >= nums[i+1] && i >=0)
    {
        i--;
    }
    if(i>=0)
    {
        let j =n-1;
        while(nums[j]<=nums[i] && j>0) j--;
        //console.log(i,j);
        swap(nums, i, j);
        reverse(nums, i+1,n-1);   
    }
    else
    {
        reverse(nums, 0,n-1);
    }
    return ;
};
function swap(nums: number[], i: number, j:number): void 
{
    let temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp; 
}
function reverse(nums: number[], i: number, j:number): void 
{
    let n = j-i+1;
    for(let k =0; k<n/2; k++)
    {
        let temp = nums[k+i];
        nums[k+i] = nums[j-k];
        nums[j-k] = temp;
    }
}