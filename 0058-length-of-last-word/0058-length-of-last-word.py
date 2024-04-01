class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing and leading whitespaces
        
        s = s.strip()
        # Find the index of the last space character
        last_space_index = s.rfind(' ')
        
        # If no space is found, return the length of the string
        if last_space_index == -1:
            return len(s)
        # Otherwise, return the length of the last word
        return len(s) - last_space_index - 1