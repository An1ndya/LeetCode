class Solution {
public:
    int total=0;
    int climbStairs(int n) 
    {
        int ara[n+2];
        ara[1] = 1;
        ara[2] = 2;
        for(int i=3;i<=n;i++)
        {
            ara[i] = ara[i-1] + ara[i-2];
        }
        
        return ara[n];
    }
};