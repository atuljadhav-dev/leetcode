class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        vowels="aeiouAEIOU"
        arr=[""]*len(s)
        while left<=right:
            if s[left] in vowels:
                while s[right] not in vowels:
                    arr[right]=s[right]
                    right-=1 
                arr[left]=s[right]
                arr[right]=s[left]
                right-=1
            else:
                arr[left]=s[left]
            left+=1
        return "".join(arr)