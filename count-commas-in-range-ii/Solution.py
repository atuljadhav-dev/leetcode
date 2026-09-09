class Solution:
    def countCommas(self, n: int) -> int:
        count=1
        t=1000
        while n>=t:
            count+=n-t+1
            t*=1000
        return count-1