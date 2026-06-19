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
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        for i in range (0,len(neg)):
            neg[i]=neg[i]*neg[i]
            
        for i in range(0, len(pos)):
            pos[i]=pos[i]*pos[i]
        i=0
        j=len(neg)-1
        while i<j:
            temp=neg[i]
            neg[i]=neg[j]
            neg[j]=temp
            j-=1
            i+=1
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