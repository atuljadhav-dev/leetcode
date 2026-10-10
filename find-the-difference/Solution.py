class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        req={}
        for ch in s:
            req[ch]=req.get(ch,0)+1
        for ch in t:
            if ch not in req:
                return ch
            req[ch]-=1
            if req[ch]==0:
                req.pop(ch)