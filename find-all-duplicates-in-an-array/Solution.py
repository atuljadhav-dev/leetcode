class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        out=[]
        col={}
        for n in nums:
            col[n]=col.get(n,0)+1
            if col[n]==2:
                out.append(n)
        return out