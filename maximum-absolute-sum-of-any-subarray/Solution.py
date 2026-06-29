class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bestending = nums[0]
        minending = nums[0]
        res = abs(nums[0])
        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = bestending + nums[i]
            v3 = minending + nums[i]
            bestending = max(v1, v2)
            minending = min(v1, v3)
            res = max(res, bestending, abs(minending))
        return res