class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mx=max(nums)
        mn=min(nums)
        ans=[]
        nums.sort()
        for i in range(mn,mx):
            if i not in nums:
                ans.append(i)
        return ans