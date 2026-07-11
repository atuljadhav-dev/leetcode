class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        ans=-1
        for i in range(0,len(nums)-1):
            if nums[i]>=nums[i+1]:
                ans=i+1
        return ans if ans!=-1 else 0