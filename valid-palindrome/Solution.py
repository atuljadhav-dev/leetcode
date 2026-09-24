class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''
        s=s.lower()
        for ch in s:
            if 'a'<=ch<='z' or '0'<=ch<='9':
                st+=ch
        return st==st[::-1]