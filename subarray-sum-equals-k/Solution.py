class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        map = {}
        map[0] = 1
        count = 0
        for i in range(0, len(nums)):
            sum += nums[i]
            complement = sum - k
            freq = map.get(complement, 0)
            count += freq
            map[sum] = map.get(sum, 0) + 1
        return count