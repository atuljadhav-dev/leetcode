class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        ans=nums[0]
        max=0
        for i in nums:
            count[i]=count.get(i, 0)+1
            if count[i]>max:
                ans=i
                max=count[i]
        return ans