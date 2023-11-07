class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n=len(dist)
        t=[]
        for i in range(n):
            t.append(dist[i]/speed[i])
        t.sort()
        #print(t)
        c=1
        for i in range(1,n):
            if t[i]>i:
                c+=1
            else:
                break
        return c
            