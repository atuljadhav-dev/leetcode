class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        req={}
        for char in s1:
            req[char]=req.get(char, 0)+1
        required=len(req)
        window={}
        left=0
        formed=0
        for right in range(0, len(s2)):
            char=s2[right]
            window[char]=window.get(char, 0)+1
            if char in req and window [char]==req[char]:
                formed+=1
            if right-left+1>len(s1):
                l_ch=s2[left]
                if l_ch in req and window [l_ch]==req[l_ch]:
                    formed-=1
                window[l_ch]-=1
                left+=1
            if required==formed:
                return True
        return False