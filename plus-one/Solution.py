class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            carry = total // 10
            ans.append(total % 10)

        if carry:
            ans.append(carry)

        ans.reverse()
        return ans