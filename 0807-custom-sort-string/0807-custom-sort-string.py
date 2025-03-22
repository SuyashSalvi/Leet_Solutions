class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(list(s))
        res = ''
        for c in order:
            if c in count:
                res += c * count[c]
                count[c] = 0
        
        for c, i in count.items():
            if i > 0:
                res += c * i

        return res