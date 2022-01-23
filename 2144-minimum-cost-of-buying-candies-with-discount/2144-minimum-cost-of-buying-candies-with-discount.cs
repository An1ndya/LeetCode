public class Solution {
    public int MinimumCost(int[] cost) 
    {
        int n = cost.Length,t=0;
        
        Array.Sort(cost);
        
        int i=n-1;
        
        while(i>=0)
        {
            if(i-2 >= 0)
            {
                t+=cost[i]+cost[i-1];
                i=i-3;
            }
            else
            {
                t+=cost[i];
                i--;
            }
        }
        return t;
    }
}