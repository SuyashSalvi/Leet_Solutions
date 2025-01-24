class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def compatibility(student, mentor):
            return sum(s == m for s, m in zip(student, mentor))
        
        # Total number of students (and mentors)
        m = len(students)
        
        # Memoized recursive function to calculate max compatibility
        @lru_cache(None)
        def dfs(remaining_mask):
            # If all students are matched, return 0
            if remaining_mask == 0:
                return 0
            
            # Find the index of the current student (log2 of first set bit in mask)
            current_student = bin(remaining_mask).count("1") - 1
            
            max_score = 0
            # Try assigning the current student to every remaining mentor
            for mentor_idx in range(m):
                if remaining_mask & (1 << mentor_idx):
                    # Calculate the score and recurse for the remaining mentors
                    max_score = max(
                        max_score,
                        compatibility(students[current_student], mentors[mentor_idx]) +
                        dfs(remaining_mask ^ (1 << mentor_idx))
                    )
            
            return max_score
        
        # Start with all mentors available (bitmask with m bits set)
        return dfs((1 << m) - 1)