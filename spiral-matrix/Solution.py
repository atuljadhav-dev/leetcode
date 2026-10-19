class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        res = []
        i = 0
        j = 0
        while left <= right:
            while i <= right and top<=bottom:
                res.append(matrix[top][i])
                i += 1
            top += 1
            j = top

            while j <= bottom and left<=right:
                res.append(matrix[j][right])
                j += 1
            right -= 1
            i = right
            while i >= left and top<=bottom:
                res.append(matrix[bottom][i])
                i -= 1
            bottom -= 1
            j = bottom
            while j >= top and left<=right:
                res.append(matrix[j][left])
                j -= 1
            left += 1
            i = left
        return res
