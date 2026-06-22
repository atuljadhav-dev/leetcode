class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        ch = {}
        for c in text:
            ch[c] = ch.get(c, 0) + 1
        return min(
            ch.get("b", 0),
            ch.get("a", 0),
            ch.get("l", 0) // 2,
            ch.get("o", 0) // 2,
            ch.get("n", 0),
        )