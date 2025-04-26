class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle zero numerator
        if numerator == 0:
            return "0"
        res = []
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        # Work with absolutes
        n, d = abs(numerator), abs(denominator)
        # Integer part
        res.append(str(n // d))
        rem = n % d
        if rem == 0:
            return "".join(res)
        # Fractional part
        res.append(".")
        # Map remainder -> position in res
        seen = {}
        while rem and rem not in seen:
            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem // d))
            rem %= d
        if rem:  # repeating
            idx = seen[rem]
            res.insert(idx, "(")
            res.append(")")
        return "".join(res)