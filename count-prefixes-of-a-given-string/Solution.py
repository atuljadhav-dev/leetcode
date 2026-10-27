class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        count=0
        for ch in words:
            if ch==s[:len(ch)]:
                count+=1
        return count