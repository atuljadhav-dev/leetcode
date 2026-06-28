class Solution:
    def cal(self, num):
        s =0
        while num > 0:
            rem = num % 10
            s += rem * rem
            num //= 10
        return s
    def isHappy(self, n: int) -> bool:
        slow=fast=n
        while True :
            slow=self.cal(slow)
            fast=self.cal(self.cal(fast))
            if slow==fast:
                if slow==1 :
                    return True
                return False
        