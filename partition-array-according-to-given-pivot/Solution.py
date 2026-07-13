class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s=[]
        l=[]
        count=0
        for i in nums:
            if i<pivot:
                s.append(i)
            elif i>pivot:
                l.append(i)
            else:
                count+=1
        dup=[pivot]*count
        return s+dup+l