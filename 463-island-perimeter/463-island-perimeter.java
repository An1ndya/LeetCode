class Solution {
    public int islandPerimeter(int[][] grid) 
    {
        int m,n,premieter=0,i,j;
        m = grid.length;
        n = grid[0].length;
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                if(grid[i][j]==1)
                {
                    if(i==0) premieter++;
                    if(i==m-1) premieter++;
                    if(j==0) premieter++;
                    if(j==n-1) premieter++;
                    
                    if(i+1<m)
                    {
                        if(grid[i+1][j]==0) premieter++;
                    }
                    if(i>0)
                    {
                        if(grid[i-1][j]==0) premieter++;
                    }
                    if(j+1<n)
                    {
                        if(grid[i][j+1]==0) premieter++;
                    }
                    if(j>0)
                    {
                        if(grid[i][j-1]==0) premieter++;
                    }
                }
            }   
        }
        return premieter;
    }
}