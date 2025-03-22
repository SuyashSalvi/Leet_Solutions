class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        charToIndex = {}

        i = 0
        for j in range(n):
            if s[j] in charToIndex:
                i = max(charToIndex[s[j]], i)
            res = max(res, j - i + 1)
            charToIndex[s[j]] = j + 1

        return res