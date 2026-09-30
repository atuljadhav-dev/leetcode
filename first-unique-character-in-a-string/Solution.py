class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch={}
        for i in range(0,len(s)):
            ch[s[i]]=ch.get(s[i],0)+1
        for i in range(0,len(s)):
            if ch[s[i]]==1:
                return i
        return -1