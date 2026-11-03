class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        for i in "!?',;.":
            paragraph=paragraph.replace(i," ")
        paragraph=paragraph.split()
        freq={}
        m=0
        res=""
        
        for w in paragraph:
            w=w.lower()
            freq[w]=freq.get(w,0)+1
            if freq[w]>m and w not in banned:
                m=freq[w]
                res=w
        print(freq)
        return res
        