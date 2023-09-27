class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        n=len(s)
    
        i=0
        while i<n:
            start=i

            while i<n and s[i]!=" " :
                i+=1
                
            if start!=i : ans = s[start:i]+ " " + ans
            else: i+=1
        
        return ans[:-1]
            
        