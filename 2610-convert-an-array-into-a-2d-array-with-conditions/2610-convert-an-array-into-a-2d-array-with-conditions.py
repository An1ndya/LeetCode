class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[[nums[0]]]
        curRow=0
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                curRow+=1
                if curRow == len(ans):
                    ans.append([nums[i]])
                else:
                    ans[curRow].append(nums[i])
            else:
                curRow=0
                ans[curRow].append(nums[i])
        return ans
                    
                
            