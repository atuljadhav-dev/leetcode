class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minval = float("inf")
        for i in range(0, len(nums)):
            if nums[i] == target:
                minval = min(abs(i - start), minval)
        return minval