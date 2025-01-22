class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        # DP array to store the length of the longest alternating subsequence ending at each index
        dp = [1] * n
        # Path array to reconstruct the subsequence
        prev = [-1] * n

        # Fill the DP array
        for i in range(1, n):
            for j in range(i):
                if groups[i] != groups[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # Find the index of the maximum value in dp
        max_index = dp.index(max(dp))

        # Reconstruct the subsequence
        result = []
        while max_index != -1:
            result.append(words[max_index])
            max_index = prev[max_index]

        # Reverse the result to get the correct order
        result.reverse()
        return result