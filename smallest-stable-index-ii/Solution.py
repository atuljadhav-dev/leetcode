class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        suff = [0] * n
        suff[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] < suff[i + 1]:
                suff[i] = nums[i]
            else:
                suff[i] = suff[i + 1]
        curr_max = nums[0]
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
                
            if curr_max - suff[i] <= k:
                return i

        return -1