class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        left = 0
        right = 0
        ans=float('inf')
        while right < len(nums):
            s += nums[right]
            while s >= target:
                length = right - left + 1
                ans = length if ans == 0 else min(ans, length)
                s -=nums[left]
                left += 1
            right += 1
        return 0 if ans ==float('inf') else ans