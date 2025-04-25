class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[0])
        n = len(startTime)
        starts = [job[0] for job in jobs]
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            s_i, e_i, p_i = jobs[i]

            skip_profit = dp[i + 1]

            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if starts[mid] < e_i:
                    lo = mid + 1
                else:
                    hi = mid
            take_profit = p_i + dp[lo]
            dp[i] = max(skip_profit, take_profit)
        return dp[0]