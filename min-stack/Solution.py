class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = self.getMin()
        if current_min is None or val < current_min:
            current_min = val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][1]
