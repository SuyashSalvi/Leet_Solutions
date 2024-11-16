from collections import deque

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * (n - k + 1)
        dq = deque()

        for i in range(n):
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            if dq and nums[i] != nums[i - 1] + 1:
                dq.clear()

            dq.append(i)

            if i >= k - 1:
                if len(dq) == k:
                    res[i - k + 1] = nums[dq[-1]]
                else:
                    res[i - k + 1] = -1
        
        return res