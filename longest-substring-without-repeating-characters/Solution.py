class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        ch = {}
        left = 0
        for right in range(0, len(s)):
            ch[s[right]] = ch.get(s[right], 0) + 1
            while ch[s[right]] > 1:
                ch[s[left]] = ch[s[left]] - 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length