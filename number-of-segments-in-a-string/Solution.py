class Solution:
    def countSegments(self, s: str) -> int:
        s=s.split(" ")
        s=[x for x in s if x!=""]
        return len(s)