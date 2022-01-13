class Solution
{  
   
    public int orangesRotting(int[][] grid)
    {
        int m,n;
        Queue<int[]> q = new LinkedList<>();
        m = grid.length;
        n = grid[0].length;
        int size,freshcount=0,time=0;
        int[] dx = {0,0,+1,-1};
        int[] dy = {+1,-1,0,0};
        int x,y;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(grid[i][j] == 2)
                {   
                    int[] point = {i,j};
                    q.add(point);
                }
                else if(grid[i][j] == 1)
                {
                    freshcount++;
                }
            }  
        }
        
        while(!q.isEmpty())
        {
            size = q.size();
            for(int i=0;i<size;i++)
            {
                int[] current = q.peek();
                q.poll();
                for(int j=0;j<4;j++)
                {
                    x = current[0] + dx[j];
                    y = current[1] + dy[j];
                    if(x < 0 || x > m-1 ||y < 0 || y > n-1 || grid[x][y] == 0 || grid[x][y] == 2) continue;
                    // grid[x][y]  is 1,should be 2
                    grid[x][y] = 2;
                    freshcount--;
                    int[] point = {x,y};
                    q.add(point);
                }

            }
            //if queue empty then no new adjacent tomatto rotted, should time should not increase
            if(!q.isEmpty()) time++;
        }
        if(freshcount > 0) return -1;
        return time;    
    }  
}