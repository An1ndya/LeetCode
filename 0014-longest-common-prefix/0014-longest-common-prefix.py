class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans= ""
        n=len(strs)
        minlen = 200
        for i in range(n):
            if len(strs[i])<minlen: minlen = len(strs[i])
                
        for i in range(minlen):
            for j in range(n-1):
                if strs[j][i] != strs[j+1][i]:
                    return ans;                    
            ans+=strs[0][i]        
        return ans