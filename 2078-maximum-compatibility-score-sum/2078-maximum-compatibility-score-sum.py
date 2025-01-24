class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])

        @functools.cache
        def dp(student, mentor):
            if student == m:
                return 0
            
            res = 0
            for i in range(m):
                if mentor & (1 << i): continue
                score = sum(1 for j in range(n) if students[student][j] == mentors[i][j])
                res = max(res, score + dp(student + 1, mentor | (1 << i)))

            return res
        return dp(0, 0)