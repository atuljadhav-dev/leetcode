# time complexity O(n^2)
# space complexity O(n)
# slicing requires space and time n
# class Solution:
#     def firstStableIndex(self, nums: list[int], k: int) -> int:
#         for i in range(0,len(nums)):
#             if k>=max(nums[:i+1])-min(nums[i:len(nums)]):
#                 return i
#         return -1


# time complexity O(n)
# space complexity O(1)
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