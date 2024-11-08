class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        DAY, WEEK, MONTH = costs[0], costs[1], costs[2]
        cache = {}
        def dp(i) -> int:
            print("i",i)
            if i in cache: return cache[i]
            if i > len(days) - 1: return 0
            # 1. day choice
            day_choice = DAY + dp(i+1)
            # 2. week choice
            j = i
            while j < len(days) and days[i] + 7 > days[j]: j += 1
            week_choice = WEEK + dp(j)
            # 3. month choice
            j = i
            while j < len(days) and days[i] + 30 > days[j]: j += 1
            month_choice = MONTH + dp(j)
            cache[i] = min(day_choice, week_choice, month_choice)
            return cache[i]
        return dp(0)