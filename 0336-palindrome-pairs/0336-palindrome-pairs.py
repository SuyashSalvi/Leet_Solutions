class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words_map = {word : i for i, word in enumerate(words)}
        print(words_map)
        answers = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                prefix, suffix = word[:j], word[j:]
                
                # If prefix is palindrome, reverse the suffix and check if that exists
                if prefix == prefix[::-1]:
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in words_map and i != words_map[reversed_suffix]:
                        answers.append([words_map[reversed_suffix],i])
                
                # To avoid duplicates, make sure j != len(word)
                if j != len(word) and suffix == suffix[::-1]:
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in words_map and i != words_map[reversed_prefix]:
                        answers.append([i,words_map[reversed_prefix]])

        return answers    