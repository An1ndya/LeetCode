class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maxarea=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]!=0 and i>0:
                    matrix[i][j]+= matrix[i-1][j]
                    
            #without copy matrix[i] will be also sorted       
            colheight = matrix[i].copy()
            colheight.sort(reverse=True)
            
            for j in range(n):
                maxarea = max(maxarea, colheight[j]*(j+1))
        return maxarea
                