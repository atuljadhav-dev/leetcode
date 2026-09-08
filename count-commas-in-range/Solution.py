class Solution:
    def countCommas(self, n: int) -> int:
        return n-999 if n-999>0 else 0