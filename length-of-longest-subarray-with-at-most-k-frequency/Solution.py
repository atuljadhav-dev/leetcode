class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        window={}
        maxLen=-1
        start=0
        for i in range(0,len(nums)):
            num=nums[i]
            window[num]=window.get(num,0)+1
            while window[num]>k:
                lnum=nums[start]
                window[lnum]-=1
                start+=1
            maxLen=max(maxLen,i-start+1)
        return maxLen