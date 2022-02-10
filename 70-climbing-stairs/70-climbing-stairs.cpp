class Solution {
public:
    int climbStairs(int n) 
    {
        int ara[n+2];
        ara[1] = 1;        //1 step
        ara[2] = 2;         //1+1,2 : 2 combination 
        for(int i=3;i<=n;i++)
        {
            //come to point i by climbing 1 step from i-1
            //or by climbing 2 step from i-2
            //so it can reach by sum total of i-1 and i-2's combination 
            ara[i] = ara[i-1] + ara[i-2];
        }
        
        return ara[n];
    }
};