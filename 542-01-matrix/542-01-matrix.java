class Solution 
{    
    public int[][] updateMatrix(int[][] mat) 
    {
        int m,n,max,min;
        m = mat.length;
        n = mat[0].length;
        max=m+n;
        int[][] updatedMatrix = new int[m][n];
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(mat[i][j] == 0) updatedMatrix[i][j] = 0;
                else updatedMatrix[i][j] = max;
            }  
        }
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(mat[i][j] == 1)
                {
                    if(i > 0) updatedMatrix[i][j] = Math.min(updatedMatrix[i][j],updatedMatrix[i-1][j]+1);
                    if(j > 0) updatedMatrix[i][j] = Math.min(updatedMatrix[i][j],updatedMatrix[i][j-1]+1);
                }
            }  
        }
        //needed to up from both side so minimum value updated
        for(int i=m-1;i>=0;i--)
        {
            for(int j=n-1;j>=0;j--)
            {
                if(mat[i][j] == 1)
                {
                    if(i < m-1) updatedMatrix[i][j] = Math.min(updatedMatrix[i][j],updatedMatrix[i+1][j]+1);
                    if(j < n-1) updatedMatrix[i][j] = Math.min(updatedMatrix[i][j],updatedMatrix[i][j+1]+1);
                }
            }  
        }
        return updatedMatrix;
    }
}