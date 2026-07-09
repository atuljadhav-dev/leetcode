class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for s in strs:
            if len(prefix)>len(s):
                prefix=prefix[0:len(s)]
            l=len(s)if len(prefix)>len(s) else len(prefix)
            for i in range(0, l):
                if prefix[i]!=s[i]:
                    prefix=prefix[0:i]
                    break
            
            if len(prefix)==0:
                break
        return prefix