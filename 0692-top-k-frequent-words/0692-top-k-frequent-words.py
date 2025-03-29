class Trie:
    def __init__(self):
        self.children = {}   # Maps character to Trie node.
        self.is_word = False # Indicates the end of a valid word.

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.is_word = True

    def get_words(self, prefix: str, k_left: List[int]) -> List[str]:
        """
        Retrieve words in lexicographical order from the trie starting at this node.
        k_left is a one-element list acting as a mutable integer representing the number
        of words still needed.
        """
        result = []
        if self.is_word:
            # If this node marks the end of a word, include it.
            if k_left[0] > 0:
                result.append(prefix)
                k_left[0] -= 1
            # If we've reached k words, stop.
            if k_left[0] == 0:
                return result

        # Traverse children in alphabetical order.
        for c in sorted(self.children.keys()):
            if k_left[0] == 0:
                break
            result.extend(self.children[c].get_words(prefix + c, k_left))
        return result


from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        cnt = Counter(words)
        # Create a bucket array where each index represents a frequency.
        # Each bucket will store a Trie containing words with that frequency.
        bucket = [None] * (n + 1)
        
        for word, freq in cnt.items():
            if bucket[freq] is None:
                bucket[freq] = Trie()
            bucket[freq].insert(word)
        
        res = []
        # k_left is a mutable container to allow the trie traversal to decrease the count.
        k_left = [k]
        # Process buckets in descending frequency order.
        for freq in range(n, 0, -1):
            if k_left[0] == 0:
                break
            if bucket[freq] is not None:
                # Get words from the trie in lex order.
                res.extend(bucket[freq].get_words("", k_left))
        return res