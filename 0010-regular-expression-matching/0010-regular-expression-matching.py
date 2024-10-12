class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if not p:
        #     return not s

        # first_match = bool(s) and p[0] in {s[0],"."}

        # if len(p) >= 2 and p[1] == "*":
        #     return(
        #         #zero present s[0]
        #         self.isMatch(s, p[2:])
        #         or
        #         # more than zero present of s[0]
        #         first_match and self.isMatch(s[1:],p)
        #     )

        # else:
        #     return first_match and self.isMatch(s[1:], p[1:])


        memo = {}

        def dp(i: int,j: int) -> bool:
            if(i,j) not in memo:
                
                if not bool(p[j:]): 
                    ans = i == len(s)
                else:
                    first_match = bool(s[i:]) and p[j] in {s[i],"."}
                    if bool(p[j+1:]) and p[j+1] == "*":
                        ans = dp(i,j+2) or first_match and dp(i+1,j)
                    else:
                        ans = first_match and dp(i+1,j+1)
                memo[i,j] = ans
            return memo[i, j]
        return dp(0,0) 