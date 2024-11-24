class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum, neg_count = 0, 0
        min_neg_val = float("inf")

        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    neg_count += 1
                min_neg_val = min(min_neg_val, abs(val))

        if neg_count % 2 != 0:
            total_sum -= 2 * min_neg_val

        return total_sum