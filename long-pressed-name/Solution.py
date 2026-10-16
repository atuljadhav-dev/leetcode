class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        j=0
        if name[0]!=typed[0]:
            return False
        while i<len(typed):
            # ch match increment pointer
            if j<len(name) and name[j]==typed[i]:
                j+=1
            # ch not equal to previous name ch i.e.  alex and aaleexa extra a
            elif name[j-1]!=typed[i]:
                return False
            i+=1
        return j==len(name)