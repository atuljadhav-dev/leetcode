class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = right = 0
        window_product = 1
        count = 0
        while right < len(nums):
            window_product *= nums[right]
            if nums[right] < k:
                count += 1
            else:
                right += 1
                left = right
                window_product = 1
                continue
            while window_product >= k:
                window_product //= nums[left]
                left += 1
            count += right-left
            right += 1
        return count