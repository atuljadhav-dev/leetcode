class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        req = {}
        for word in words:
            req[word] = req.get(word, 0) + 1
        ans = []
        l =len(words[0])
        required = len(req) 
        for i in range(0, l):
            left=i
            formed=0
            window={}
            for right in range(i, len(s), l):
                word = s[right : right + l]
                if len(word)!=l:
                    break
                window[word] = window.get(word, 0) + 1
                if word in req and window[word] == req[word]:
                    formed += 1
                if right - left + l > len(words) * l:
                    w = s[left : left + l]
                    if w in req and window[w] == req[w]:
                        formed -= 1
                    window[w] -= 1
                    left += l
                if required == formed:
                    ans.append(left)
                
        return ans