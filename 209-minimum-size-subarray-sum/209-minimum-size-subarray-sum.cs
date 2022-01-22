public class Solution {
    public int MinSubArrayLen(int target,int[]nums) {
        
        int n = nums.Length; 
        int l=0, r=0, minlen = 100000, sum = 0;
        
        while(r < n)
        { 
            sum += nums[r];
            r++;
            while(sum >= target)
            {
                int len = r-l;
                if (len < minlen )  minlen = len;
                sum -= nums[l];
                l++; 
            }
            
        }
        if (minlen != 100000) return minlen;
        else return 0;
    }
}