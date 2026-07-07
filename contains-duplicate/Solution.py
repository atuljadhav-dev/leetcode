class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup={}
        for i in nums:
            dup[i]=dup.get(i, 0)+1
            if dup[i]>1:
                return True
        return False