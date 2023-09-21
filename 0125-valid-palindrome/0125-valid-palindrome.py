class Solution:
    def isPalindrome(self, s: str) -> bool:

        onlyaplha = ""
        for i in s:
            if i.isalnum(): 
                onlyaplha+= i
        onlyaplha = onlyaplha.lower()
        
        n = len(onlyaplha)
        l=0
        r=n-1
        while l<r:
            if onlyaplha[l]!=onlyaplha[r]:
                return False
            l+=1
            r-=1
        return True