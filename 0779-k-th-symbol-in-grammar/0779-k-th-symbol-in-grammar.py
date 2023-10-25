class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k==1 : return 0
        if n==1 : return 0
        if k%2==1: 
            if self.kthGrammar(n-1,(k+1)//2) ==0:
                return 0
            else:
                return 1
        else: 
            if self.kthGrammar(n-1,k//2) == 0:
                return 1
            else:
                return 0