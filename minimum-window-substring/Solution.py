class Solution:
    def minWindow(self, s: str, t: str) -> str:
        req={}
        for char in t:
            req[char]=req.get(char, 0)+1
        required=len(req)
        window={}
        left=start=0
        formed=0
        min_length=float('inf')
        for right in range(0,len(s)):
            char=s[right]
            window[char]=window.get(char, 0)+1
            if char in req and window [char]==req[char]:
                formed+=1
            while left<=right and required==formed:
                char_left=s[left]
                if right-left+1<min_length:
                    min_length=right-left+1
                    start=left
                window[char_left]-=1
                if char_left in req and window[char_left]<req[char_left]:
                     formed-=1
                left+=1
        return "" if min_length==float('inf') else s[start:start+min_length]