class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        flag=len(nums)/3
        ans=[]
        for num in nums:
            count[num]=count.get(num, 0)+1
            if count[num]>flag and num not in ans:
                ans.append(num)
        return ans