class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n

        for i in range(1,n):
            for j in range(i):
                if groups[i] != groups[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        max_value_index = dp.index(max(dp))
        ans = []
        while max_value_index != -1:
            ans.append(words[max_value_index])
            max_value_index = prev[max_value_index]

        ans.reverse()
        return ans