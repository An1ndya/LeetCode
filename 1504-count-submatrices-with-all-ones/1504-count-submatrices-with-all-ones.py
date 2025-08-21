class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        width = [[0] * n for _ in range(m)]
        
        # Step 1: compute width array
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    width[i][j] = (width[i][j-1] if j > 0 else 0) + 1
        
        res = 0
        # Step 2: count submatrices
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                min_width = width[i][j]
                for k in range(i, -1, -1):
                    if width[k][j] == 0:
                        break
                    min_width = min(min_width, width[k][j])
                    res += min_width
        return res