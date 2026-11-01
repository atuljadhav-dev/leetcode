class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                res = 0
                if i == "+":
                    res = a + b
                elif i == "-":
                    res = a - b
                elif i == "/":
                    res = a / b
                elif i == "*":
                    res = a * b
                stack.append(int(res))
        return stack[-1]
