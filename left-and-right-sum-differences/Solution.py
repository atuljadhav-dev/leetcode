class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        ans=[]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        suffix = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]
        for i in range(len(nums)):
            ans.append(abs(prefix[i] - suffix[i]))
        return ans