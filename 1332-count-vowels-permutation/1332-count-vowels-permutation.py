class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        MOD = 10 ** 9 + 7

        for _ in range(1,n):
            aa = (e + u + i) % MOD
            ee = (a + i) % MOD
            ii = (e + o) % MOD
            oo = (i) % MOD
            uu = (o + i) % MOD

            a, e, i, o, u = aa, ee, ii, oo, uu

        return (a + e + i + o + u) % MOD