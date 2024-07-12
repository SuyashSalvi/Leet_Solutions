class Solution:
    def betterCompression(self, compressed: str) -> str:
        d = {}
        i, n = 0, len(compressed)
        
        while i < n:
            x = compressed[i]
            i += 1
            curr = 0
            while i < n and compressed[i].isnumeric():
                curr = curr * 10 + int(compressed[i])
                i += 1
            if x in d:
                d[x] += curr
            else:
                d[x] = curr
        
        return ''.join(f'{char}{d[char]}' for char in sorted(d))