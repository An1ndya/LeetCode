public class Solution {
    public bool IsInterleave(string s1, string s2, string s3) {
        int n = s1.Length;
        int m = s2.Length;
        int o = s3.Length;
        if( o!=n+m){ return false;}
        
        bool[,] dp = new bool[n+1,m+1];
        
        dp[0,0]=true;
        for(int i=1;i<=n;i++)
        {
            dp[i,0]=dp[i-1,0] && s1[i-1]==s3[i-1];
        }
        for(int j=1;j<=m;j++)
        {
            dp[0,j]=dp[0,j-1] && s2[j-1]==s3[j-1];
        }
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                dp[i,j]=(dp[i-1,j] && s1[i-1]==s3[i+j-1]) || (dp[i,j-1] && s2[j-1]==s3[i+j-1]);
            }
        }
            
        return dp[n,m];
    }
}