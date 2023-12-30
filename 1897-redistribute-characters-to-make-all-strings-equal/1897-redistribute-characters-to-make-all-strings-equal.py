from collections import defaultdict
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n=len(words)
        charcount = defaultdict(int) 
        for word in words:
            for char in word:
                charcount[char]+=1
        for key in charcount.keys():
            if charcount[key]%n!=0:
                return False
        return True