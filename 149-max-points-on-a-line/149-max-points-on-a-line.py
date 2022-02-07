class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        if n==1: return 1
        if n==2: return 2
        mx=0
        for i in range(n):
            d={}
            h=1
            v=1
            for j in range(i+1,n):
                if points[i][0]==points[j][0]:
                    h+=1
                    mx=max(mx,h)
                elif points[i][1]==points[j][1]:
                    v+=1
                    mx=max(mx,v)
                else:
                    dx=points[i][0]-points[j][0]
                    dy=points[i][1]-points[j][1]
                    gcd=math.gcd(dx,dy)
                    dx, dy = dx/gcd, dy/gcd
                    if dx<0: dx, dy = -dx,-dy
                    slope=str(dx)+","+str(dy)
                    if slope in d:
                        d[slope]+=1
                    else:
                        d[slope]=2
                    mx=max(mx,d[slope])
            
        return mx