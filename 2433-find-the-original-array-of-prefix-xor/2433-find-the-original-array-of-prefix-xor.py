class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        #pref[i] ^ pref[i-1] = arr[i]
        #to do in place we need to iterate right to left
        for i in range(len(pref)-1,0,-1):
            pref[i]^=pref[i-1]
        return pref