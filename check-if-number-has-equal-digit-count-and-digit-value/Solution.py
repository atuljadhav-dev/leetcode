class Solution:
    def digitCount(self, num: str) -> bool:
        count={}
        for i in num:
            i=int(i)
            count[i]=count.get(i,0)+1
        for i in range(0,len(num)):
            if count.get(i,0)!=int(num[i]):
                return False
        return True