class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        mx= m+n-2
        fact=[1]*(mx+1)

        for i in range(2,mx+1,1):
            fact[i]=fact[i-1]*i
            
        ans=int(fact[mx]/(fact[m-1]*fact[n-1]))
        return ans
    
        