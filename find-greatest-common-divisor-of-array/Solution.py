class Solution:
    def gcd(a,b):
        if a%b==0:
            return b
        gcd(a%b,b)
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        min=nums[0]
        max=nums[len(nums)-1]
        return gcd(max,min)