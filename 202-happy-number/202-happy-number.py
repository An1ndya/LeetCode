class Solution:
    def isHappy(self, n: int) -> bool:
        d={}
        while True:
            #print(n)
            if n == 1 : return True
            if n in d : return False
            d[n]=True
            t=n
            n=0
            while t!=0:
                digit=t%10
                n+=digit*digit
                t=int(t/10)