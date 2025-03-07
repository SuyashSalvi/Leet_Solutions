class Solution:
    def _sieve(self, upperBound):
        prime = [True] * (upperBound + 1)
        prime[0] = prime[1] = False
        for i in range(2, int(upperBound**0.5) + 1):
            if prime[i]:
                for j in range(i * i, upperBound + 1, i):
                    prime[j] = False
        
        return prime



    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = self._sieve(right)
        prime = [num for num in range(left, right + 1) if sieve[num]]
        res = [-1, -1]

        if len(prime) < 2:
            return res
        dif = float('inf')
        for i in range(1,len(prime)):
            curDif = prime[i] - prime[i - 1]
            if curDif < dif:
                dif = curDif
                res[0], res[1] = prime[i - 1], prime[i]
        return res