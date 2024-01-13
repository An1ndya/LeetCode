class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCharCount = defaultdict(int)
        tCharCount = defaultdict(int)
        Alluniquechar = {} 
        for char in s:
            sCharCount[char]+=1
            Alluniquechar[char] = True
        for char in t:
            tCharCount[char]+=1
            Alluniquechar[char] = True
        ans=0
        for char in Alluniquechar.keys():
        
            #cases needed mandatory change
            if sCharCount[char] > tCharCount[char]:
                
                ans += sCharCount[char]-tCharCount[char]
            # if oposite occur we dont need to do anything 
            # cause previous counted operations automatically reduce extra char in t
        return ans