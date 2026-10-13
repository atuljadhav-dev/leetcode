class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[x*x for x in nums]
        nums.sort()
        i=0
        s=0
        j=len(nums)-1
        while i <j:
            # add max nums and remove min num
            s+=nums[j]-nums[i]
            i+=1
            j-=1
        if i==j:
            s+=nums[i]
        return s