class Solution {
    public int m,n,max=0,area; 
    
    public int maxAreaOfIsland(int[][] grid)
    {
        m = grid.length;
        n = grid[0].length;
        boolean isvisited[][] = new boolean[m][n];
        //Arrays.fill(isvisited, false);
        for(int a = 0; a < isvisited.length; a++){
            for(int b = 0; b < isvisited[a].length; b++){
                isvisited[a][b] = false;
            }
        }
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(!isvisited[i][j])
                {
                    if(grid[i][j] == 1)
                    {
                        area = 0;
                        DFS(grid,i,j,isvisited);
                        if(area>max) max=area;
                    }
                }            
            }
        }
        return max;
    }
    public void DFS(int[][] grid, int i,int j,boolean[][] isvisited)
    {

        if(i<0 || i>=m) return;
        if(j<0 || j>=n) return;
        if(isvisited[i][j] == true) return;
        if(grid[i][j] == 0)
        {
            isvisited[i][j] = true;
            return;
        }
        else if(grid[i][j] == 1){
            area++;
            isvisited[i][j] = true;
            DFS(grid,i+1,j,isvisited);
            DFS(grid,i-1,j,isvisited);
            DFS(grid,i,j+1,isvisited);
            DFS(grid,i,j-1,isvisited);
        } 
        
    
    }
}