function sortArrayByParity(nums: number[]): number[] 
{
    let n = nums.length;
    let k =0;
    while(k<n && nums[k]%2==0){k++;}
    let firstodd = k;
    let cur = k+1;
    for(let i =k+1;i<n;i++)
    {
        if(nums[i]%2==0 && firstodd<i)
        {
            swap(nums,firstodd,i);
            while(firstodd<n && nums[firstodd]%2==0){firstodd++;}
        }
    }
    return nums;
};
function swap(nums,i,j):void
{
    let temp=nums[i];
    nums[i]=nums[j];
    nums[j]=temp;
}