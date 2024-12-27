class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # entire idea is to find: left score -> (value[i] + i) + right score -> (value[j] - j)
        n = len(values)
        max_left_score = values[0]
        max_score = 0
        for i in range(1,n):
            cur_right_score = values[i] - i
            max_score = max(max_score, max_left_score + cur_right_score)
            max_left_score = max(max_left_score, values[i] + i)

        return max_score