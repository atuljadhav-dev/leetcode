class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        sum = 0
        for i in range(0, len(nums)):
            if i % 2 == 0:
                sum += nums[i]
            else:
                sum -= nums[i]
        return sum
