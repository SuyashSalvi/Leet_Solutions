class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        @functools.cache
        def cntV(n, s):
            total = 1
            if n > 1:
                if s == 'a':    
                    total = (cntV(n-1, 'e') + cntV(n-1, 'u') + cntV(n-1, 'i')) % MOD
                elif s == 'e':
                    total = (cntV(n-1, 'a') + cntV(n-1, 'i')) % MOD
                elif s == 'i':
                    total = (cntV(n-1, 'e') + cntV(n-1, 'o')) % MOD
                elif s == 'o':
                    total = (cntV(n-1, 'i')) % MOD
                else:
                    total = (cntV(n-1, 'o') + cntV(n-1, 'i')) % MOD
            return total

        return sum(cntV(n,v) for v in 'aeiou') % MOD