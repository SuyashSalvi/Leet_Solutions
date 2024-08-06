class Solution(object):
    def myAtoi(self, s):
        if len(s) == 0:
            return 0

        i, sign, ans = 0, 1, 0
        max_int, min_int = 2**31 - 1, -2**31
        while i < len(s) and s[i] == " ":
            i += 1

        if i < len(s) and s[i] in "-+":
            if s[i] == "-":
                sign = -1
            i += 1
        
        while i < len(s) and '0' <= s[i] <= '9':
            d = ord(s[i]) - ord('0')
            if ans > max_int // 10 or (ans == max_int // 10 and d > max_int % 10):
                return max_int if sign == 1 else min_int
            ans = ans * 10 + d
            i += 1
        return ans * sign