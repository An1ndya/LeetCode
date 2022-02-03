class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n=len(nums1)
        ijsum = {}
        ans=0
        for i in nums1:
            for j in nums2: 
                if i+j in ijsum:
                    ijsum[i+j] += 1
                else:
                    ijsum[i+j] = 1
        for k in nums3:
            for l in nums4: 
                if -k-l in ijsum:
                    ans += ijsum[-k-l]
        return ans