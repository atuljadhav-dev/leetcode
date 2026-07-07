class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx={}
        for i in range(0, len(nums)):
            if nums[i] in idx and i-idx[nums[i]]<=k:
                return True
            idx[nums[i]]=i
        return False