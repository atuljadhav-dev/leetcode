class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ch={}
        for c in s:
            ch[c]=ch.get(c, 0)+1
        for c in t:
            ch[c]=ch.get(c, 0)-1
            if ch[c]<0:
                return False
            if ch[c]==0:
                ch.pop(c)
        return len(ch)==0