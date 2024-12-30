class Solution:
    def numWays(self, words, target):
        freq_map = [[0] * 26 for _ in range(len(words[0]))]
        dp = [[-1] * len(target) for _ in range(len(words[0]))]

        # Creating frequency map for each index of the word
        for word in words:
            for i in range(len(words[0])):
                freq_map[i][ord(word[i]) - 97] += 1

        return self._get_possibilities(words, target, freq_map, 0, 0, dp)



    def _get_possibilities(self, words, target, freq_map, wordIndex, targetIndex, dp):
        # Base cases -------------------------------------:
        # 1. if we have coivered the entire target successfully, add 1 to ans counter
        if targetIndex == len(target):
            return 1
        # 2. if we exhausted max word's length or remaining length of target is more than that of remaining word's length we can't proceed further, hence can't add to the ans counter
        if (wordIndex == len(words[0])) or (len(target) - targetIndex > len(words[0]) - wordIndex):
            return 0

        # Memoization check -------------------------------------:
        if dp[wordIndex][targetIndex] != -1:
            return dp[wordIndex][targetIndex]

        
        # Recursive calculation -------------------------------------:
        countWays = 0
        curPos = ord(target[targetIndex]) - 97

        # 1. if we skip the current word Index, to get all the possibilities
        countWays += self._get_possibilities(words, target, freq_map, wordIndex + 1, targetIndex, dp)

        # 2. if we consider the current word Index
        countWays += self._get_possibilities(words, target, freq_map, wordIndex + 1, targetIndex + 1, dp) * freq_map[wordIndex][curPos]


        dp[wordIndex][targetIndex] = countWays % 1000000007

        return dp[wordIndex][targetIndex]