class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            u=num%10
            t=num//10
            num=u+t
        return num