class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans=[]
        count={}
        for i in range(0, len(s)):
            sl=s[i:i+10]
            count[sl]=count.get(sl,0)+1
            if count[sl]>1 and sl not in ans:
                ans.append(sl)               
        return ans