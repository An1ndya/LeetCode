class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        transpose=[]
        for j in range(n):
            row=[]
            for i in range(m):
                row.append(matrix[i][j])
            transpose.append(row)
        return transpose