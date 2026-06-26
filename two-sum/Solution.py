class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(0, len(nums)):
            rem=target-nums[i]
            if rem in seen.keys():
                return [i, seen[rem]]
            seen[nums[i]]=i
        return []