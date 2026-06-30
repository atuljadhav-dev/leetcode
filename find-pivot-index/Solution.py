class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        total = sum(nums)
        if total-nums[0]==0:
            return 0
        for i in range(1, len(nums)):
            left += nums[i - 1]
            right = total - left - nums[i]
            if left == right: 
                return i
        return -1