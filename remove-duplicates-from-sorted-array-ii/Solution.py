class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 2  
        for j in range(2,len(nums)):
            if nums[i - 2] != nums[j]:
                nums[i] = nums[j]
                i += 1    
        return i