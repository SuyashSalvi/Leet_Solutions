class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        remaining = sum(piles)
        memo = {}
        return self.__is_next_person_winner(piles, remaining, memo)

    def __is_next_person_winner(self, piles, remaining, memo):
        key = "-".join(map(str, piles))

        if key in memo:
            return memo[key]

        if remaining == 0:
            return False

        for i in range(len(piles)):
            for j in range(1, piles[i] + 1):
                piles[i] -= j
                next_state = sorted(piles)
                if not self.__is_next_person_winner(next_state, remaining - j, memo):
                    memo[key] = True
                    return True
                piles[i] += j
        memo[key] = False
        return False
