class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<2:
            return 0
        ans=0
        for i in range(1, len(nums)):
            ans=max(ans, nums[i]-nums[i-1])
        return ans