class Solution {
    public int searchInsert(int[] nums, int target)
    {
       // if(target < nums[0]) return 0;
        
        int l,r, m, p; 
        l = 0;
        r = nums.length - 1;
        p = l + (r - l) / 2;
        
        while (l <= r) {
             m = l + (r - l) / 2;

            if (nums[m] == target)
            
                return m;

            if (nums[m] < target)
            {    
                l = m + 1;
                p = m + 1;
            }
            else
            {
                r = m - 1;
                p = m;
            }
        }

        return p; //return index position if inserted not existing element 
    }
}