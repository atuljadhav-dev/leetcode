class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ch={}
        for i in range(0, len(s)):
            ch[s[i]]=ch.get(s[i],t[i] if t[i] not in ch.values() else None)
            if ch[s[i]]!=t[i]:
                return False
        return True