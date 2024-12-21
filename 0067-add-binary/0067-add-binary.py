class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a,2), int(b,2)
        while y:
            ans = x^y
            y = (x&y)<<1
            x = ans
        return bin(x)[2:]