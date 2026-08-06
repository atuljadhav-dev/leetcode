class Solution:
    def smallestNumber(self, n: int, t: int) -> int:  
        while True:
            last_digit = n % 10
            remaining = n // 10

            if remaining == 0:
                if last_digit % t == 0:
                    return n
            else:
                if (last_digit * remaining) % t == 0:
                    return n

            n += 1