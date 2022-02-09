class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(1,numRows):
            col=[]
            col.append(1)
            for j in range(1,i):
                col.append(ans[i-1][j-1]+ans[i-1][j])
            col.append(1)
            ans.append(col)
        return ans