class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=s.split(" ")
        while arr[len(arr)-1]=="":
              arr.pop()
        return len(arr[len(arr)-1])