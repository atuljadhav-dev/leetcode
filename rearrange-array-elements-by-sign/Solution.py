class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else :
                neg.append(i)
        ans=[]
        left=0
        right =0
        while left<len(pos) or right <len(neg):
            if len(ans)%2==0:
                ans.append(pos[left])
                left+=1
            else:
                ans.append(neg[right])
                right+=1
        return ans