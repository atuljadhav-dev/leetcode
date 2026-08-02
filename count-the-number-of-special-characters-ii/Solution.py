class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        low=[-1]*26
        up=[-1]*26
        for i in range(0,len(word)):
            ch=word[i]
            if ord(ch)>96:
                low[ord(ch)-97]=i
            else:
                up[ord(ch)-65]=i if up[ord(ch)-65]==-1 else up[ord(ch)-65]
        print(low,up)
        for i in range(0,len(low)):
            if low[i]!=-1 and low[i]<up[i]:
                count+=1
        return count