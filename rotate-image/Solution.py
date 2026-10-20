class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        while i < len(matrix):
            j = i + 1
            while j < len(matrix):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j += 1
            i += 1
        for i in range(0, len(matrix)):
            left = 0
            right = len(matrix[0]) - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                right-=1
                left+=1
