class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def subseq(s,t):
            if len(s) == 0:
                return True
            i = 0
            while i < len(t) and s[0] != t[i]:
                i += 1
            if i > len(t) - 1:
                return False
            return subseq(s[1:], t[i + 1:])
            
        return subseq(s, t)
            