class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx=abs(fx-sx)
        dy=abs(fy-sy)
        
        #same destination and source
        if dx==0 and dy==0 and t==1: return False
        
        mn=min(dx,dy)
        mx=max(dx,dy)
        
        #first min move diagonally and then max-min move axis wise
        mint=mn+(mx-mn)
        
        return mint<=t