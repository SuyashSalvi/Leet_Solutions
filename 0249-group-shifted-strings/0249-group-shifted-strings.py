from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_hash(s):
            key = []
            for a, b in zip(s,s[1:]):
                key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            return ''.join(key)

        groups = defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)

        return list(groups.values())