class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        if m*n!=r*c: return mat
        ans=[[0]*c for i in range(r)]
        p,q=0,0
        for i in range(m):
            for j in range(n):
                ans[p][q]=mat[i][j]
                q+=1
                if q%c==0:
                    q=0
                    p+=1
        return ans