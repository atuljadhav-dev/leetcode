class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        window={}
        j=0
        maxL=float('-inf')
        for i in range(0,len(s)):
            ch=s[i]
            window[ch]=window.get(ch,0)+1
            while window[ch]>2 and j<i:
                lch=s[j]
                window[lch]-=1
                j+=1
            maxL=max(maxL,i-j+1)
        return maxL