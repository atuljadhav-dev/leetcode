class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i=1
        arr=[]
        while i<=n:
            if i%5==0 and i%3==0:
                arr.append("FizzBuzz")
            elif i%5==0:
                arr.append("Buzz")
            elif i%3==0:
                arr.append("Fizz")
            else:
                arr.append(str(i)) 
            i+=1
        return arr