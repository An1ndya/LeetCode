class Solution:
    def isPathCrossing(self, path: str) -> bool:
        i,j=0,0
        hashpoint={"0,0":True}
        for c in path:
            if c=='N': j+=1
            elif c=='S': j-=1
            elif c=='E': i+=1
            elif c=='W': i-=1
                
            point = str(i)+ "," + str(j)
            #print(point)
            if point in hashpoint:
                return True
            hashpoint[point] = True
        return False