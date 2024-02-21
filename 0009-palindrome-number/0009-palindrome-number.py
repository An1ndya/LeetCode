class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        arr = []
        while x > 0:
            #take the last digit 
            remainder = x % 10
            arr.append(remainder)
            #get next number excluding last digit 
            x = x // 10

        n = len(arr)
        
        for i in range(n//2):
            #check with mirror point 
            #if dont match then not pallindrome
            if arr[i] != arr[n-1-i]:
                return False 
        #loop passed, so a palindrome  
        return True