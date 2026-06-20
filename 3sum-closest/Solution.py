class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff=float('inf')
        ans=0
        for i in range(0, len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]+nums[i]
                diff=abs(sum-target)
                if sum ==target:
                    return sum 
                elif sum < target:
                    if diff < min_diff:
                        min_diff = diff
                        ans=sum
                    left += 1
                else:
                    if diff < min_diff:
                        min_diff = diff
                        ans=sum
                    right -= 1
        return ans