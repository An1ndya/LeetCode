class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        maskcount = [0]*1024 # 2^10 possible values of mask
        maskcount[0] = 1     # 0 mask means all even, so a count have found
        ans = 0
        mask = 0
        for letter in word:
            #mask for 0 to current position
            mask ^= 1 << (ord(letter)-97)
            #if same mask previous occur means we find a substring between them
            # substring count should be count of time that mask previously occured
            ans += maskcount[mask]
            #increase mask occurance count
            maskcount[mask] += 1
            #check if between them odd char exist and that mask count is already found
            for odd_bit in range(10):
                oddmask = mask ^ (1 << odd_bit) 
                #if oddmask not found 0
                #if found count of that occurance add to answer
                ans += maskcount[oddmask]
        return ans
            