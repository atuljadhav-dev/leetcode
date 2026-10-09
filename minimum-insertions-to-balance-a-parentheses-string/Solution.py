class Solution:
    def minInsertions(self, s: str) -> int:
        count=0
        res=0
        i=0
        while i<len(s):
            if s[i]=='(':
                # add opening bracket
                count+=1
                i+=1
            elif s[i]==')' and i<len(s)-1 and s[i+1]==')':
                if count>0:
                    # if there are continues to closing bracket remove the open bracket
                    count-=1
                else:
                    # if there is no opening bracket for continues 2 closing bracket need to add 1 opening bracket
                    res+=1
                i+=2
            else:
                if count>0:
                    # if there is openly one closing bracket then need to add the one closing bracket and remove the one opening bracket
                    count-=1
                    res+=1
                else:
                    # if there is only one closing bracket and no respective opening bracket need to add one opening and one closing bracket
                    res+=2
                i+=1
        if count>0:
            # if there are still some opening bracket then need to add 2x closing bracket
            res+=count*2
        return res