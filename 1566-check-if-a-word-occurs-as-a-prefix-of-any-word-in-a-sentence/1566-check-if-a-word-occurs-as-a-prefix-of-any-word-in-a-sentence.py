class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        i, word_pos = 0, 1  # Initialize index and word position

        while i < len(sentence):
            # Check if the current word starts with searchWord
            if sentence[i:i + len(searchWord)] == searchWord and (i == 0 or sentence[i - 1] == " "):
                return word_pos

            # Move to the next word
            while i < len(sentence) and sentence[i] != " ":
                i += 1
            i += 1  # Skip the space
            word_pos += 1  # Increment word position

        return -1  # Return -1 if no match is found
