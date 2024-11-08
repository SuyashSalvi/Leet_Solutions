class Solution:
    # @lru_cache
    # def recursiveMemo(self, index, s):
    #     if index == len(s):
    #         return 1
        
    #     if s[index] == "0":
    #         return 0
        
    #     if index == len(s) - 1:
    #         return 1

    #     ans = self.recursiveMemo(index+1, s)
    #     if int(s[index:index+2]) <= 26:
    #         ans += self.recursiveMemo(index+2, s)

    #     return ans
    def numDecodings(self, s: str) -> int:
        # return self.recursiveMemo(0, s)

        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]

            two_digit = int(s[i-2:i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i-2]    
        return dp[len(s)]