class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False]* n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for dif in range(1,n):
            for i in range(n-dif):
                j = i + dif
                if s[i] == s[j]:
                    if dif == 1 or dp[i+1][j-1] == True:
                        dp[i][j] = True

        
        def backtrack(start,path):
            if start == n:
                res.append(path[:])
            for end in range(start,n):
                if dp[start][end]:
                    backtrack(end+1,path+[s[start:end+1]])
        
        res = []
        backtrack(0,[])
        return res