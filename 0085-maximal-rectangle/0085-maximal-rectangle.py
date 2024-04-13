class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        height = [0]*col        #colwise height of 1s
        leftboundary = [0]*col  #rowise left boundary containing 1s rec
        rightboundary = [col]*col #rowise right boundary containing 1s rec
        maxArea = 0
        for i in range(row):
            rowleftB = 0 
            rowrightB = col
            for j in range(col):
                if matrix[i][j] == '1':
                    height[j] += 1
                    leftboundary[j] = max(leftboundary[j], rowleftB)
                else:
                    height[j] = 0
                    leftboundary[j] = 0     # as height becomes zero its area is 0
                    rowleftB = j+1          #update  next col check
            #calculate from right
            for j in range(col-1,-1,-1):
                if matrix[i][j] == '1':
                    rightboundary[j] = min(rightboundary[j], rowrightB)
                else:
                    rightboundary[j] = col    #as height becomes zero its area is 0
                    rowrightB = j             #update for next col
            
            for j in range(col):      
                maxArea = max(maxArea,(rightboundary[j]-leftboundary[j])*height[j]);
        
        return maxArea