public class Solution {
    bool[] iswin = new bool[100001];
    public bool WinnerSquareGame(int n) 
    {
        return DFS(n);
    }
    public bool DFS(int n)
    {
        if(iswin[n]){
            return iswin[n];  
        }
        else{
            bool ans= false;
            for(int i=1;i*i<=n;i++)
            {
                if(n==i*i)
                {
                    iswin[n] = true;
                    return true;    
                }else{  
                    //if previous point is false then this move will result no remaining stone;win
                    ans = ans || !DFS(n-i*i); 
                    if(ans)
                    {
                        iswin[n] = true;
                        return true;  
                    } 
                }
            }
            iswin[n] = ans;
            return ans;
        }
    }
}