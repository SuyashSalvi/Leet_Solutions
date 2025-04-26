from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Map each reversed word to its index
        rev_map = {word[::-1]: i for i, word in enumerate(words)}
        ans = []

        def is_pal(s: str) -> bool:
            # Check palindrome in O(len(s))
            return s == s[::-1]

        # For each word, try every split
        for i, w in enumerate(words):
            L = len(w)
            for k in range(L+1):
                pref, suf = w[:k], w[k:]

                # Case 1: pref is palindrome -> need rev_suf on left
                if is_pal(pref):
                    j = rev_map.get(suf)
                    if j is not None and j != i:
                        ans.append([j, i])

                # Case 2: suf is palindrome -> need rev_pref on right
                # k < L avoids duplicating the empty‐prefix case twice
                if k < L and is_pal(suf):
                    j = rev_map.get(pref)
                    if j is not None and j != i:
                        ans.append([i, j])

        return ans