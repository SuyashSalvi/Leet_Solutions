class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        def __game(piles, remaining,memo):
            key = '-'.join(map(str,piles))
            if key in memo:
                return memo[key]
            
            if remaining == 0:
                return False

            # going through all the states
            for i in range(len(piles)):
                # considering all the permutations
                for j in range(1, piles[i]+1):
                    piles[i] -= j
                    
                    next_state = sorted(piles)
                    if not __game(next_state,remaining-j,memo):
                        memo[key] = True
                        return True
                    piles[i] += j
            memo[key] = False
            return False

        remaining = sum(piles)
        memo = {}
        return __game(piles,remaining,memo)
    
        