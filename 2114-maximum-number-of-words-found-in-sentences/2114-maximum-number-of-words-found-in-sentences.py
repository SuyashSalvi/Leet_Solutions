class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        for sentence in sentences:
            words = sentence.split()
            max_count = max(max_count, len(words))
        return max_count