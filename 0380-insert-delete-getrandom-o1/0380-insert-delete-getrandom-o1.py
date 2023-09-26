import random
class RandomizedSet:
            
    def __init__(self):      
        self.hash = {}
        
    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        else:
            self.hash[val] = True
            return True

    def remove(self, val: int) -> bool:
        if val in self.hash:
            del self.hash[val]
            return True
        else:
            return False

    def getRandom(self) -> int:

        return random.choice(list(self.hash))
      


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()