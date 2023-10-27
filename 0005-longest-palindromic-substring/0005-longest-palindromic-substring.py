class Solution:
    def longestPalindrome(self, s: str) -> str:
        mxlen=0
        start=end=0
        n =len(s)
        for i in range(0,n,1):
            odd = self.find(s,i,i,n)
            if odd[1]-odd[0]> mxlen: 
                mxlen = odd[1]-odd[0]
                start,end = odd[0], odd[1]
            
            even = self.find(s,i,i+1,n)
            if even[1]-even[0]> mxlen: 
                mxlen = even[1]-even[0]
                start,end = even[0], even[1]
        
        return s[start:end+1]
    
    def find(self,s,i,j,n):
        while(i>=0 and j<n and s[i]==s[j]):
            i-=1
            j+=1
        return [i+1,j-1]   #j-i+1-1+1