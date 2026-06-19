class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=j=0
        merge=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                merge.append(nums1[i]) 
                i+=1
            else:
                merge.append(nums2[j])
                j+=1 
        while i<len(nums1):
            merge.append(nums1[i])
            i+=1
        while j<len(nums2):
            merge.append(nums2[j])
            j+=1
        rem=len(merge)%2
        if rem==0:
            return (merge[(len(merge)//2)-1]+merge[(len(merge)//2)]) /2
        else:
            return merge[len(merge)//2]
            
            