class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        #sort elements
        nums.sort()
        print(nums)
        n=len(nums)
        #check if possible
        #if first and last of any 3 sequential element 
        #have difference greater that k then 
        #as sorted so middle element's difference will definitely less than k
        for i in range(2,n,3):
            if nums[i] - nums[i-2] > k :
                return []
        ans = []
        for i in range(n//3):
            ans.append(nums[i*3 : 3*i+3])
        return ans