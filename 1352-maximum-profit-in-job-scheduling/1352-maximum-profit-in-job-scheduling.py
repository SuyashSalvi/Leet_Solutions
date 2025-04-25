from typing import List

class Solution:
    def jobScheduling(
        self,
        startTime: List[int],
        endTime:   List[int],
        profit:    List[int]
    ) -> int:
        """
        Bottom-up DP + manual binary search (no bisect).
        """
        # 1) Pair up and sort jobs by start time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        n = len(jobs)
        
        # 2) Extract sorted start times for binary search
        starts = [job[0] for job in jobs]
        
        # 3) dp[i] = max profit using jobs[i..n-1]; dp[n] = 0
        dp = [0] * (n + 1)
        
        # 4) Build dp from back to front
        for i in range(n - 1, -1, -1):
            s_i, e_i, p_i = jobs[i]
            
            # Option A: skip this job
            skip_profit = dp[i + 1]
            
            # Option B: take this job
            #   find the first index j > i where starts[j] >= e_i
            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if starts[mid] < e_i:
                    lo = mid + 1
                else:
                    hi = mid
            take_profit = p_i + dp[lo]
            
            # 5) choose the better option
            dp[i] = max(skip_profit, take_profit)
        
        # 6) dp[0] is the answer
        return dp[0]