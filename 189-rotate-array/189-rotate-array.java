class Solution {
    public void rotate(int[] nums, int k) {
        int length = nums.length;
        k = k % length;
        
        int[] rotatednums = new int[length];
        
        for(int i=0;i<length;i++)
        {
             rotatednums[i] = nums[(length-k+i)%length]; 
        }
        
        for(int i=0;i<length;i++)
        {
             nums[i] = rotatednums[i]; 
        }
    }
}