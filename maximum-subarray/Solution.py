class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bestending=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=bestending+nums[i]
            bestending=max(v1,v2)
            res=max(res,bestending)
        return res