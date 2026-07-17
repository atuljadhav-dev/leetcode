class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        maxArea=0
        while left<right:
            if height[left]<height[right]:
                area=(right-left)*height[left]
                maxArea=max(maxArea,area)
                left+=1
            else:
                area=(right-left)*height[right]
                maxArea=max(maxArea,area)
                right-=1
        return maxArea