class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        onesRowi = [0 for i in range(m)]
        onesColj = [0 for i in range(n)]

        for i in range(m):
            for j in range(n):
                onesRowi[i]+=grid[i][j]
                onesColj[j]+=grid[i][j]
        #print(onesRowi)
        #print(onesColj)
        for i in range(m):
            for j in range(n):
                #onesRowi-zerosRowi=2*onesRowi-m
                #onesColj-zerosColj=2*onesColj-n
                grid[i][j]=2*onesRowi[i]-m + 2*onesColj[j]-n        
        return grid