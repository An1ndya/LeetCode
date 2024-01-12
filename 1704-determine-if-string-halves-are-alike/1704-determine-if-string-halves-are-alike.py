class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # List of vowels
        vowelList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
 
        # Using Dictionary comprehension
        vowelDict = {vowel: False for vowel in vowelList}
        
        half=len(s)//2
        count=0
        for i in range(half*2):
            if s[i] in vowelDict:
                if i< half:
                    #increase count for first halves
                    count+=1
                else:
                    #decrease count for second halves
                    count-=1
        #print(vowelDict)

        return count==0