class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        mx=0
        l=[0]*n
        r=[0]*n
        l[0]=-1
        r[n-1]=n
        for i in range(1, n, 1):
            p=i-1
            while p>-1 and heights[i] <= heights[p]:
                p=l[p]
            l[i]=p
        for i in range(n-2,-1,-1):
            p=i+1
            while p<n and heights[i] <= heights[p]:
                p=r[p]
            r[i]=p
        for i in range(0,n,1):
            w = r[i]-l[i]-1
            area = w*heights[i]
            if area>mx:
                mx=area
        return mx
        
        