public class Solution {
    public void MoveZeroes(int[] nums) {
        int length = nums.Length;
        int numberofzero = 0;

        for(int i = 0; i< length; i++)
        {
            if(nums[i] == 0) numberofzero++;
        }
        for(int i = length-1; i >= 0 ; i--)
        {
            for(int j = 0; j < i; j++)
            {
                if(nums[j] == 0)
                {   
                    nums[j]   = nums[j+1];
                    nums[j+1] = 0;
                }
            }          
        }
    }
}