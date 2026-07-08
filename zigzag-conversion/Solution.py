class Solution:
    def convert(self, s: str, numRows: int) -> str:
        op = ""
        if numRows == 1 or numRows>=len(s):
            return s
        diff = numRows + numRows - 2 
        for i in range(0, numRows):
            op += s[i]
            next = diff - i
            if next==i:
                next+=diff
            k = next - i
            while next < len(s):
                op += s[next]
                next += diff if diff == k or k == 0 else diff - k
                k = diff - k
        return op
