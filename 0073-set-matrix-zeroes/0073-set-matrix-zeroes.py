class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        firstrow = False
        firstcol = False
            
        #set first row and col to zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i==0:  firstrow = True
                    if j==0:  firstcol  = True
                    matrix[0][j]=0
                    matrix[i][0]=0
                    
        #assign all zero except first row and first col           
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
                    
        #check if all first or col will be zero or not
        #previous attempt to this might temper other col or row         
        if firstrow:
            for j in range(n):
                matrix[0][j]=0
                
        if firstcol:
            for i in range(m):
                matrix[i][0]=0                 