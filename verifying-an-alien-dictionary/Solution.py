class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        alpha = {}
        for i in range(0, len(order)):
            # store index and ch
            alpha[order[i]] = i
        for i in range(1, len(words)):
            # get two words
            w1, w2 = words[i - 1], words[i]           
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    # find first non matching ch
                    if alpha[w1[j]] > alpha[w2[j]]:
                        # if ch of w1 is greter than ch of w2 return false
                        return False
                    break  #stop execution for current w1 and w2
            else:
                # if all the ch of w1 and w2 are same then check length word with smaller length should come first
                if len(w1) > len(w2):
                    return False
                    
        return True