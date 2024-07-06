class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur = 1
        reverse = False
        while time > 0:
            if reverse:
                cur = cur-1 
                if cur == 0:
                    cur  = 2
                    reverse = False
            else:
                cur = cur + 1
                if cur == n+1:
                    cur  = n-1
                    reverse = True
            time -= 1
        return cur