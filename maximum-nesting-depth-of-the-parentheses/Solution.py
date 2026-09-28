class Solution:
    def maxDepth(self, s: str) -> int:
        stack=0
        maxDepth=0
        for ch in s:
            if ch == '(':
                stack+=1
                if stack>maxDepth:
                    maxDepth=stack
            elif ch == ')':
                stack-=1   
        return maxDepth