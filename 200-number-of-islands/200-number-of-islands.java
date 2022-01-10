class Solution {
    public int m,n,sum=0; 
    public int numIslands(char[][] grid)
    {
        m = grid.length;
        n = grid[0].length;
        boolean isvisited[][] = new boolean[m][n];

        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(!isvisited[i][j])
                {
                    if(grid[i][j] == '1')
                    {
                        DFS(grid,i,j,isvisited);
                        sum++;
                    }
                    else{
                        isvisited[i][j] = true;
                    }
                }            
            }
        }
        return sum;
    }
    public void DFS(char[][] grid, int i,int j,boolean[][] isvisited)
    {

        if(i<0 || i>=m || j<0 || j>=n) return;
        
        if(isvisited[i][j] == true) return;
        
        isvisited[i][j] = true;
        
        if(grid[i][j] == '0')   return;
        
        DFS(grid,i+1,j,isvisited);
        DFS(grid,i-1,j,isvisited);
        DFS(grid,i,j+1,isvisited);
        DFS(grid,i,j-1,isvisited);
        
    }
}