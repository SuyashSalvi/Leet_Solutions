class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # entire idea is to find: left score -> (value[i] + i) + right score -> (value[j] - j)
        n = len(values)
        max_scores = [0] * n
        max_score = 0
        max_scores[0] = values[0] # max left score of 1st element is values[0] - 0
        for i in range(1,n):
            cur_right_score = values[i] - i
            max_score = max(max_score, max_scores[i-1] + cur_right_score)
            max_scores[i] = max(max_scores[i-1], values[i] + i)

        return max_score