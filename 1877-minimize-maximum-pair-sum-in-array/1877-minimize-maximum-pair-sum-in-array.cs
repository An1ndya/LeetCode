public class Solution {
    public int MinPairSum(int[] nums) 
    {
        int n=nums.Length;
        Array.Sort(nums);
        int max=0;
        for(int i=0;i<n/2;i++)
        {
            max = Math.Max(max , nums[i]+nums[n-1-i]);
        }
        return max;
        
    }
}