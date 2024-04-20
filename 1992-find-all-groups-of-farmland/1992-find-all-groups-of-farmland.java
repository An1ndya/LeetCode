class Solution {
    public int m,n,sum=0; 
    public int[] rectangle;
    public boolean isvisited[][];
    public int[][] findFarmland(int[][] land) 
    {
        m = land.length;
        n = land[0].length;
        isvisited = new boolean[m][n];
        ArrayList<int[]> rectangles = new ArrayList<>();

        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(!isvisited[i][j])
                {
                    if(land[i][j] == 1)
                    {
                        //found a farmland
                        rectangle = new int[]{i, j, i, j};
                        DFS(land,i,j);
                        rectangles.add(rectangle);
                        sum++;
                    }
                    else{
                        isvisited[i][j] = true;
                    }
                }            
            }
        }
        //convert from arraylist to 2d array
        int[][] ans = new int[sum][4];
        for(int i=0;i<sum;i++){
            
            for(int j=0;j<4;j++){
                ans[i][j] = rectangles.get(i)[j]; 
            }
        }
        return ans;
    }
    public void DFS(int[][] grid, int i,int j)
    {

        if(i<0 || i>=m || j<0 || j>=n) return;
        
        if(isvisited[i][j] == true) return;
        
        isvisited[i][j] = true;
        
        if(grid[i][j] == 0)   return;
        //as retacngle max and minimum have bottom-right and top-left cordinate
        rectangle[0] = Math.min(rectangle[0], i);
        rectangle[1] = Math.min(rectangle[1], j);
        rectangle[2] = Math.max(rectangle[2], i);
        rectangle[3] = Math.max(rectangle[3], j);
            
        DFS(grid,i+1,j);
        DFS(grid,i-1,j);
        DFS(grid,i,j+1);
        DFS(grid,i,j-1);  
    }
}