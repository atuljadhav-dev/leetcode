class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        ch = {}
        max_length = 0
        max_ch = 0
        for right in range(0, len(s)):
            ch[s[right]] = ch.get(s[right], 0) + 1
            max_ch = max(max_ch, ch[s[right]])
            while right - left + 1 - max_ch > k:
                ch[s[left]] = ch[s[left]] - 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
        