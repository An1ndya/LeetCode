class Solution:
    mx=0
    def integerBreak(self, n: int) -> int:
        if n==2: return 1
        elif n ==3 : return 2
        elif n==4 : return 4
        p=1
        while n>4:
            n -=3
            p *=3
        p=p*n
        
        return p
