class MinStack:

    def __init__(self):
        self.stack = []
        self.min=sys.maxsize
        self.n=0

    def push(self, val: int) -> None:
        if val < self.min : self.min = val
        
        self.stack.append([val,self.min])
        self.n+=1
        return 
    
    def pop(self) -> None: 
        self.stack.pop()
        self.n+=-1
        if self.n==0: self.min=sys.maxsize
        else: self.min = self.stack[-1][1]
        return None
    
    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()