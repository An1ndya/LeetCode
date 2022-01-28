public class Solution {
    int m,n;
    public bool Exist(char[][] board, string word) {
        m = board.Length;
        n=board[0].Length;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                bool[,] isvisited = new bool[m,n];
                if (DFS(ref board,ref word,i,j,0,ref isvisited)) return true;
            }
        }
        return false;
    }
    public bool DFS(ref char[][] board,ref string word,int i,int j,int index,ref bool[,] isvisited)
    {
        
        if(board[i][j]==word[index] && !isvisited[i,j])
        {
            if(index+1==word.Length) return true;
            
            isvisited[i,j] = true;
            int[,] dir= {{0,0,1,-1},{1,-1,0,0}};
            bool ans=false;
            for(int k=0;k<4;k++)
            {
                int x= i +dir[0,k];
                int y= j +dir[1,k];
                if(!(x>=m || x <0 || y<0 ||y>=n))
                {
                    ans |= DFS(ref board,ref word,x,y,index+1,ref isvisited);
                    if(ans) return ans;
                }
            }
            isvisited[i,j] = false;
        }
        return false;   
    }
}