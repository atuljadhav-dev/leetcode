class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        count = 0
        max_j = len(grid[0])  
        col_sums = [0] * max_j

        for row in grid:
            row_sum = 0
            for j in range(max_j):
                row_sum += row[j]
                col_sums[j] += row_sum
        
                if col_sums[j] > k:
                    max_j = j 
                    break
            
                count += 1
        return count