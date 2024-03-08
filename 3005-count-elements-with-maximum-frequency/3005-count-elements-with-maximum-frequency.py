class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        mx = 0   # maximum frequency
        mxnumcount = 0   # count of numbers having maximum frequency 
        for num in nums:
            frequency[num] += 1
            if frequency[num] > mx:
                mx = frequency[num] 
                # new max frequency number found, set count to 1
                mxnumcount = 1
            elif frequency[num] == mx:
                # as this another max frequency number found, increase count to 1
                mxnumcount += 1
        #total frequencies of maximum frequency should be multiply of them
        return mx*mxnumcount