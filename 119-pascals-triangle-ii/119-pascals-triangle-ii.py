class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[[1 for i in range(j+1)] for j in range(rowIndex+1)]
        
        for i in range(1,rowIndex+1):
            for j in range(1,i):
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
        return ans[rowIndex]