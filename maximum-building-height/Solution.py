class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        m = len(restrictions)
        for i in range(1, m):
            id_diff = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + id_diff)
            
        for i in range(m - 2, -1, -1):
            id_diff = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + id_diff)
        max_h = 0
        for i in range(1, m):
            id_diff = restrictions[i][0] - restrictions[i-1][0]
            h_sum = restrictions[i][1] + restrictions[i-1][1]
            peak_height = (id_diff + h_sum) // 2
            max_h = max(max_h, peak_height)
        last_id, last_height = restrictions[-1]
        max_h = max(max_h, last_height + (n - last_id))
        
        return max_h