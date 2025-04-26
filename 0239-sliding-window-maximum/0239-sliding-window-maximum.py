from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Return a list of the maximums of each sliding window of size k.
        Uses a monotonic deque to achieve O(n) time.
        """
        dq = deque()  # will store indices, values in decreasing order
        res = []

        # Build initial window
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])

        # Slide the window
        for i in range(k, len(nums)):
            # Evict indices out of this window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            # Maintain decreasing order in deque
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            # Front is the max for this window
            res.append(nums[dq[0]])

        return res
