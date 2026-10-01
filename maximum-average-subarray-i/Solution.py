class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left=0
        right=k
        max_sum=s=sum(nums[:k])
        while right<len(nums):
            s=s+nums[right]-nums[left]
            max_sum=max(max_sum,s)
            left+=1
            right+=1
        return max_sum/k