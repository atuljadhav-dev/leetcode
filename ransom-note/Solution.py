class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        mg={}
        for ch in magazine:
            mg[ch]=mg.get(ch,0)+1
        for ch in  ransomNote:
            if ch in mg:
                mg[ch]-=1
                if mg[ch]==-1:
                    return False
            else:
                return False
        return True