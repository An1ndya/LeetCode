public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        int p;
        int l;
        int r;
        int minlen;
        int sum;
        
		
        p =nums.Length;
 
        l=0; r=0; minlen = 100000; sum = nums[0];
        
        while(l <= r)
        {
            if(sum >= target)
            {
                int len = r-l + 1;
                if (len < minlen )  minlen = len;
            }
            
            if (r < p){
                r++;
                sum += nums[r];
            }else{
                sum -= nums[l];
                l++;             
            }
        }
        return minlen;
    }
}