class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freqs = [0] * 3 # frequency of a,b,c
        n = len(s)

        for c in s:
            freqs[ord(c) - ord('a')] += 1
        # right and left ar relative position of remainig window 
        # need to maximize right - left 
        left = 0   
        right = 0   
        if freqs[0] < k or freqs[1] < k or freqs[2] < k:
            return -1

        for right in range(n):
            #omit element 
            freqs[ord(s[right]) - ord('a')] -= 1
            
            # if current remainig window dont have k number of a,b,c
            # we  need to increase left
            # cause remainig window cannot be more large
            # so left should be increase along with right
            # so size of middle window right - left + 1 need to be same 
            # for if not case we can still increase right 
            if freqs[0] < k or freqs[1] < k or freqs[2] < k:
                freqs[ord(s[left]) - ord('a')] += 1
                left += 1
            

            #print(left,s[left], right,s[right])
        # remaining window length  = right - left + 1
        # here left and right ar actual index but relative position of maximum remaining window 
        return n - (right - left + 1)
            