class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n==1: return [nums[0]*nums[0]]
        
        allnegative =  False
        allpositvie =  False
        left = 0
        right = 1
        #if last number negative or zero means all are negative
        if nums[n-1] <= 0:  
            allnegative = True
            left = n-2
            right = n-1
        #if first number positive or zero meansall are positivr
        elif nums[0]>=0:
            allpositvie =  True
            left = 0
            right = 1
        # check if all elements are positve and negative
        # 0 is considered nuertal for efficiency
        if not (allpositvie and allpositvie):
            #contain both positve and negative
            #check pointer for both direction 
            for i in range(1,n):
                if nums[i-1] < 0 and  nums[i] >= 0 :
                    left = i-1
                    right = i
                    break
        ans=[]
        count = 0
        while count < n:
            #check if both pointer valid
            if left >= 0 and right <n:
                sqrleft = nums[left]*nums[left]
                sqrright = nums[right]*nums[right]
                #compare minimum
                if sqrleft < sqrright:
                    ans.append(sqrleft)
                    left-=1
                else:
                    ans.append(sqrright)
                    right+=1
                
            elif left >= 0:
                ans.append(nums[left]*nums[left])
                left-=1
            else:
                ans.append(nums[right]*nums[right])
                right+=1    
            count += 1
        return ans