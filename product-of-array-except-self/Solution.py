class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = 1
        res=[1]*len(nums)
        for i in range(-2, -len(nums) - 1, -1):
            # store the product from end excluding the current num
            res[i] = res[i + 1] * nums[i + 1]
        for i in range(0, len(nums)):
            # multiply the prefix multiplication excluding current num 
            res[i]=pre*res[i]
            pre*=nums[i]
        return res