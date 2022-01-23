class Solution {
    public int n,sum = 0;
    public int findCircleNum(int[][] isConnected) {
        n = isConnected.length;
        boolean isvisited[] = new boolean[n];

        for(int i=0;i<n;i++)
        {
            if(!isvisited[i])
            {
                DFS(isConnected,i,isvisited);
                sum++;
            }                  
        }
        return sum;
    }
    public void DFS(int[][] isConnected, int i,boolean[] isvisited)
    {
        if(i<0 || i>n) return;
        
        if(isvisited[i] == true) return;
        
        isvisited[i] = true;
        
        for(int j=0;j<n;j++)
        {
            if(isConnected[i][j] == 1 && !isvisited[j])
            {
                DFS(isConnected,j,isvisited);
            }              
        }    
    }
}