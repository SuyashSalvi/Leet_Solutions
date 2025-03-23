class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def countPalindromesAround(s, l, h):
            count = 0
            while l >= 0 and h < len(s):
                if s[l] != s[h]:
                    break
                l -= 1
                h += 1
                count += 1
            return count

        for i in range(len(s)):
            res += countPalindromesAround(s, i, i)
            res += countPalindromesAround(s, i, i + 1)
        return res

