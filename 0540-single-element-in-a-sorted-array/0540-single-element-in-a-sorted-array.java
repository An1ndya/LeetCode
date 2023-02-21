class Solution {
    public int singleNonDuplicate(int[] nums) {
        int n = nums.length;
        int low=0;
        int high =n-1;
        int mid =0;
        while(low<high)
        {
            mid = (int)(low+high)/2;
            if(mid%2==0 && nums[mid]==nums[mid+1])
            {
                low=mid+1;
            }
            else if(mid%2==1 && nums[mid]==nums[mid-1])
            {
                low=mid+1;
            }
            else
            {
                high=mid;
            }
        }
        return nums[low]; //Or high
    }
}