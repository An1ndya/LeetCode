class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n=len(points)
        arrows=1
        points = sorted(points,key=lambda x: (x[0],x[1]))
        #pass 1st arrow with last x psotion of ballon
        # cause Xend might hit other overlapping ballon as they are sorted
        arrowX=points[0][1]
        
        for i in range(1,n):
            if arrowX < points[i][0]:
                #current ballon is not overlapped with previous ballon
                #so we need to throw a new arrow
                arrows += 1
                #last x position of ballon as our arrowX
                #same reason, so we may burst overlapping ballon lies front
                arrowX = points[i][1]
            else:
                #the ballon overlapped 
                #so we will adjust arrow x such that 
                # it pass one of ballon's end position which is minimum 
                #minimum cause to misplace the arrow for next overlapping condition 
                #means arrow covers the first ballon always 
                arrowX = min(arrowX,points[i][1])
        return arrows