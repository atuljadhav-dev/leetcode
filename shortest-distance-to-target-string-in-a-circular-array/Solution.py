class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        minDist=float('inf')
        for i in  range(0,len(words)):
            if words[i]==target:
                rd=abs(startIndex-i)
                ld=len(words)-rd
                minDist=min(rd,ld,minDist)
        return minDist if minDist != float('inf') else -1
                    