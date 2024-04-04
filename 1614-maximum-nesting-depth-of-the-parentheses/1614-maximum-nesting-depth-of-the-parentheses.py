class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        mx = 0
        depth = 0
        for char in s:
            if char == '(':
                stack.append(char)
                depth += 1
                mx = max(mx, depth)
            elif char == ')':
                #as s is VPS, so a ( must be present
                stack.pop()
                depth -= 1
            
        return mx
            