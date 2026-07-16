class Solution:
    def gcd(a,b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd=[]
        mx=float('-inf')
        for i in range(0,len(nums)):
            mx=max(mx,nums[i])
            prefixGcd.append(gcd(nums[i],mx))
        prefixGcd.sort()
        i=0
        sum=0
        while i<len(prefixGcd)//2:
            sum+=gcd(prefixGcd[i],prefixGcd[len(prefixGcd)-1-i])
            i+=1
        return sum