class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        neg=[]
        pos=[]
        for i in range(0,len(nums)):
            if nums[i]<0:
                neg.append(nums[i]*nums[i])
            else:
                pos.append(nums[i]*nums[i])
        
        neg=neg[::-1]
        j=i=0
        res=[]
        while i<len(neg) and j<len(pos):
            if neg[i]<pos[j]:
                res.append(neg[i])
                i+=1
            else:
                res.append(pos[j])
                j+=1
        while i<len(neg):
            res.append(neg[i])
            i+=1  
        while j<len(pos):
            res.append(pos[j]) 
            j+=1 
        return res