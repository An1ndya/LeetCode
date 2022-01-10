class Solution {
    int m,n,oldcolor,newcolorglobal;
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        oldcolor =  image[sr][sc];
        newcolorglobal = newColor;
        m = image.length;
        n = image[0].length;
        DFS(image,sr,sc);
        return image;
    }
    public void DFS(int[][] image, int i,int j)
    {
        if(i<0 || i>=m) return;
        if(j<0 || j>=n) return;
        if(oldcolor == newcolorglobal) return;
        
        if(image[i][j] == oldcolor){
            
            image[i][j] = newcolorglobal;
            DFS(image,i+1,j);
            DFS(image,i-1,j);
            DFS(image,i,j+1);
            DFS(image,i,j-1);
        }     
    }
}