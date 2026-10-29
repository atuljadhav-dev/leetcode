class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = 0
        for ch in s:
            total += ord(ch) - ord("a") + 1
        preSum = 0
        for ch in s:
            preSum += ord(ch) - ord("a") + 1
            if total - preSum == preSum:
                return True
        return False
