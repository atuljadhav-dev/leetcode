class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        score = 0
        rows = len(nums)
        cols = len(nums[0])

        for c in range(cols):
            mx = 0
            for r in range(rows):
                mx = max(mx, nums[r][c])
            score += mx

        return score