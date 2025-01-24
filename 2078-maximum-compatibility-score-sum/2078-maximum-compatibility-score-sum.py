class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)

        def compatibility_score(student, mentor):
            return sum(s ==     m for s,m in zip(student, mentor))

        @lru_cache(None)
        def dfs(remaining_mask):
            if remaining_mask == 0: return 0

            cur_student = bin(remaining_mask).count("1") - 1
            res = 0
            for i in range(m):
                if remaining_mask & (1 << i):
                    res = max(res, compatibility_score(students[cur_student],mentors[i]) + dfs(remaining_mask ^ (1 << i)))
            return res

        return dfs((1 << m) - 1)