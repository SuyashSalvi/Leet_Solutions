class Solution:
    def betterCompression(self, compressed: str) -> str:
        d, i, n = {}, 0, len(compressed)
        while i < n: 
            x, curr = compressed[i], ''
            while i+1<n and compressed[i+1].isnumeric():
                i += 1
                curr += compressed[i]
            if x in d.keys():
                d[x] += int(curr)
            else:
                d[x] = int(curr)
            i +=1
            
        return ''.join(x+str(d[x]) for x in sorted(d.keys()))