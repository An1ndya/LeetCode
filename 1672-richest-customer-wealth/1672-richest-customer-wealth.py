class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=len(accounts)
        n=len(accounts[0])
        mx=0
        for i in range(0,m,1):
            w=0
            for j in range(0,n,1):
                w+=accounts[i][j]
            if w> mx:
                mx =w
        
        return mx
            