class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a','e','i','o','u'}
        prefix_sum = [0] * len(words)
        res = [0] * len(queries)
        cur_sum = 0

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                cur_sum += 1
            prefix_sum[i] = cur_sum

        for i, q in enumerate(queries):
            res[i] = prefix_sum[q[1]] - (0 if q[0] == 0  else prefix_sum[q[0]-1])

        return res