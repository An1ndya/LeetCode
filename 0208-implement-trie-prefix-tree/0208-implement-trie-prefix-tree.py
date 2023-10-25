class Trie:

    def __init__(self):
        self.root={}
        
    def insert(self, word: str) -> None:
        curchar = self.root
        for c in word:
            if c not in curchar:
                curchar[c]={}
            curchar=curchar[c]
        curchar['word']=True

    def search(self, word: str) -> bool:
        curchar = self.root
        for c in word:
            if c not in curchar:
                return False
            curchar=curchar[c]
        return 'word' in curchar

    def startsWith(self, prefix: str) -> bool:    
        curchar = self.root
        for c in prefix:
            if c not in curchar:
                return False
            curchar=curchar[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)