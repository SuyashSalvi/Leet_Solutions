class Solution:
    @lru_cache
    def recursiveMemo(self, index, s):
        if index == len(s):
            return 1
        
        if s[index] == "0":
            return 0
        
        if index == len(s) - 1:
            return 1

        ans = self.recursiveMemo(index+1, s)
        if int(s[index:index+2]) <= 26:
            ans += self.recursiveMemo(index+2, s)

        return ans
    def numDecodings(self, s: str) -> int:
        return self.recursiveMemo(0, s)

        