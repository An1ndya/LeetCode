class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n=len(points)
        c=1
        points = sorted(points,key=lambda x: (x[0],x[1]))
        #print(points)
        x=points[0][1]
        for i in range(1,n):
            if x<points[i][0]:
                c+=1
                x=points[i][1]
            else:
                x=min(x,points[i][1])
        return c