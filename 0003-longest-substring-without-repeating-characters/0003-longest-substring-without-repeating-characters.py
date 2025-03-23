class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charToIndex = {}
        for r in range(len(s)):
            if s[r] in charToIndex:
                l = max(l, charToIndex[s[r]])

            res = max(res, r - l + 1)
            charToIndex[s[r]] = r + 1

        return res