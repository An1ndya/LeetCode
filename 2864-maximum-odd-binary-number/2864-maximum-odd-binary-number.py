class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        #count of one
        one=0
        for char in s:
            if char == '1': one+=1
        ans = ""
        #to get maximum , we need maximum 1 as initial postions
        #we have to put one-1 number of 1 in front
        for i in range(one-1):
            ans+= '1'
        #n-one of 0 needs to be placed after
        for i in range(n-one):
            ans+= '0'
        #last is 1, so its become odd
        ans += '1'
        return ans 