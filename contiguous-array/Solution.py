class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c={}
        zero=0
        one=0
        max_len=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                one+=1
            else:
                zero+=1
            diff=one-zero
            if one==zero:
                max_len=max(max_len,i+1)
            elif diff not in c:
                c[diff]=i
            else:
                max_len=max(max_len,i-c[diff])
        
        if one==zero:
            max_len=len(nums)
        return max_len