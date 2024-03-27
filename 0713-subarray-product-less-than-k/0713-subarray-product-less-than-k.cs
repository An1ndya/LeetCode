public class Solution {
    public int NumSubarrayProductLessThanK(int[] nums, int k) 
    {    
        int n = nums.Length; 
        int l=0, r=0, product = 1,ans=0;
        
        while(r < n)
        { 
            product *= nums[r];
            r++;
            while(product >= k && l<r)
            {   
                product /= nums[l];
                l++; 
            }
            //for window [1:4] subarr:[1,2,3,4],[2,3,4],[3,4],[4] 
            //others window [1],[1,2],[1,2,3] already added when r =1,2,3
            ans +=  r-l; 
        }
        return ans;
    }
}