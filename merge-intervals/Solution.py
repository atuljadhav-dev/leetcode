class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        start=intervals[0][0]
        end=intervals[0][1]
        
        for i in range(1, len(intervals)) :
            s=intervals[i][0]
            e=intervals[i][1]
            if end>=s:
                end=max(end, e)
                continue
            ans.append([start, end]) 
            start=s
            end=e
        ans.append ([start, end]) 
        return ans         