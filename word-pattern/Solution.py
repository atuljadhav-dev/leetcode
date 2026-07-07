class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ch1={}
        words =s.split(" ")
        if len(pattern)!=len(words):
            return False
        for i in range(0, len(pattern)):
            ch1[pattern[i]]=ch1.get(pattern[i],words[i] if words[i] not in ch1.values() else None)
            if ch1[pattern[i]]!=words[i]:
                return False
            ch1[pattern[i]]=words[i]
        return True