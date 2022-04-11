class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) 
    {
        int m = grid.length; 
        int n = grid[0].length;
        int[] arr = new int[m*n];
        int index=0;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                arr[index] = grid[i][j];
                index++;
            }
        }
        
        rotate(arr, k);

        List<List<Integer>> ans =new ArrayList<>(m); 
        index=0;
        for(int i=0;i<m;i++)
        {
            List<Integer> row = new ArrayList<Integer>(n); 
            for(int j=0;j<n;j++)
            {
                row.add(arr[index]);
                index++;
            }
            ans.add(row);
        }
        return ans;
    }
    public void rotate(int[] nums, int k) 
    {
        int n = nums.length;
        k = k % n;
        
        reverse(nums,0,n-1);
        reverse(nums,0,k-1);
        reverse(nums,k,n-1);
    }
    public void reverse(int[] nums,int i,int j)
    {
        while(i<j)
        {
            int t=nums[i];
            nums[i]=nums[j];
            nums[j]=t;
            i++;
            j--;
        }
    }
}