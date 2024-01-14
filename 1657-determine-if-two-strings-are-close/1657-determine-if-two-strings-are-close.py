class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        
        for char in word1:
            hash1[char]+=1
        for char in word2:
            hash2[char]+=1
        keys1 = list(hash1.keys())
        keys2 = list(hash2.keys())
        keys1.sort()
        keys2.sort()
        values1 = list(hash1.values())
        values2 = list(hash2.values())
        values1.sort()
        values2.sort()

        # char count need to be symmetry
        # if not we can't convert 
        return  keys1==keys2 and values1 == values2
        
        