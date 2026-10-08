class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=''
        count=0
        for i in s:
            if i=='(':
                count+=1
                if count>1:
                    res+=i
            else:
                if count>1:
                    res+=i
                count-=1
        return res