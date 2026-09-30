class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # count num frequency [1,1,1,2,2,2,3]
        col={}
        for n in nums:
            col[n]=col.get(n,0)+1
        # store frequency in bucket {1:3,2:2,3:1}
        out=[[] for _ in range(len(nums)+1)] #len(nums) +1 due to min frequency is 1 which is stored at the index 1
        for n,f in col.items():
            out[f].append(n)
        # [[], [3], [], [1, 2], [], [], [], []]
        # iterate from back and store the last number in res 
        res=[]
        for i in range(len(out)-1,0,-1):
            for num in out[i]:
                res.append(num)
                if len(res)==k:
                    return res
        return res