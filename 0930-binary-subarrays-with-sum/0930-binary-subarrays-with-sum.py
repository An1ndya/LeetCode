class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixsumCount = defaultdict(int) #notinitiliaze value have default 0
        n = len(nums)
        prefixsum = 0
        goalarraycount = 0 #subarray count with goal sum
        for i in range(n):
            prefixsum += nums[i]
            if prefixsum == goal:
                #an occurance from 0 to i subarray
                goalarraycount += 1
            #prefixsum-goal if exists will count toward our goal sum     
            goalarraycount += prefixsumCount[prefixsum - goal]
            #this prefix sum (default 0) will increase subarraycount
            prefixsumCount[prefixsum] +=  1
        return goalarraycount