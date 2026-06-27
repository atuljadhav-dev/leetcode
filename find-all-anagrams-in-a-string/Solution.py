class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        req = {}
        for ch in p:
            req[ch] = req.get(ch, 0) + 1
        required = len(req)
        left = formed = 0
        ans = []
        window = {}
        for right in range(0, len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            if ch in req and window[ch] == req[ch]:
                formed += 1
            if right - left + 1 > len(p):
                l_ch = s[left]
                if l_ch in req and window[l_ch] == req[l_ch]:
                    formed -= 1
                window[l_ch]-=1
                left+=1
            if required==formed:
                ans.append(left)
        return ans
