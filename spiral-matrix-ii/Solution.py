class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        top = left = 0
        bottom = n - 1
        right = n - 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        k = 1
        i = 0

        while left <= right:
            while i <= right and top <= bottom:
                res[top][i] = k
                k += 1
                i += 1
            top += 1
            j = top

            while j <= bottom and left <= right:
                res[j][right] = k
                k += 1
                j += 1
            right -= 1
            i = right
            while i >= left and top <= bottom:
                res[bottom][i] = k
                k += 1
                i -= 1
            bottom -= 1
            j = bottom
            while j >= top and left <= right:
                res[j][left] = k
                k += 1
                j -= 1
            left += 1
            i = left
        return res