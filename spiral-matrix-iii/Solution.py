class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        res = []

        def add(i, j):
            if i > -1 and i < rows and j > -1 and j < cols:
                res.append([i, j])

        left =  cStart - 1
        right =  cStart + 1
        top =  rStart - 1
        bottom =  rStart + 1
        i = rStart
        j = cStart
        while len(res) < rows * cols:
            while j <= right and top <= bottom:
                add(i, j)
                j += 1
            i +=1
            right+=1
            j -= 1
            while i <= bottom and left <= right:
                add(i, j)
                i += 1
            j -=1
            bottom+=1
            i -= 1
            while j >= left and top <= bottom:
                add(i, j)
                j -= 1

            i -=1
            left-=1
            j += 1
            while i >= top and left <= right:
                add(i, j)
                i -= 1
            top-=1
            i += 1
            j+=1
        return res
