class Solution:
    def longestPalindrome(self, s: str) -> int:
        col={}
        for ch in s:
            col[ch]=col.get(ch,0)+1
        l=0
        flag=True
        for ch in col:
            l+=col[ch]//2*2
            if flag and col[ch]%2==1:
                flag=False
                l+=1
        return l