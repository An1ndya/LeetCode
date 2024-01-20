public class Solution {
    public int SumSubarrayMins(int[] arr) {
        int n  = arr.Length;
        int [] dp = new int[n];   //answer for subarray end with minimum at i index
        int prevminimumindex;
        Stack<int> monotonicstack = new Stack<int>();

        for(int i=0;i<n;i++)
        {
            while(monotonicstack.Count>0 && arr[monotonicstack.Peek()]>arr[i])
            {
                monotonicstack.Pop();
            }
            if(monotonicstack.Count>0)
            {
                prevminimumindex = monotonicstack.Peek();
                //previous minimum subarray answer 
                //plus(+) count of bigger elements consist new subarry 
                //and minimum in each of them is arr[i]
                //
                dp[i] = dp[prevminimumindex]+(i-prevminimumindex)*arr[i];
            }else{
                //prevminimumindex = -1;
                //most minimum element
                // so total new subarray with this new minimum 
                //total element count till i
                dp[i] = (i+1)*arr[i];
            }    
            dp[i] %= 1000000007;
            //dp[i] = dp[prevminimumindex]+(i-prevminimumindex)*arr[i];
            monotonicstack.Push(i);
        }
        int ans=0;
        for(int i=0; i<n; i++)
        {
            ans += dp[i];
            ans %= 1000000007;
        }
        return ans;
    }
}