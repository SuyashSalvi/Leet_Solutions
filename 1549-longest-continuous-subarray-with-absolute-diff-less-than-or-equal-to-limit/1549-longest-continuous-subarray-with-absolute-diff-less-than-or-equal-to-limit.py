class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_heap = []
        min_heap = []
        left = 0
        res = 0

        for right in range(len(nums)):
            heapq.heappush(min_heap,(-nums[right],right))
            heapq.heappush(max_heap,(nums[right],right))
            while -max_heap[0][0] - min_heap[0][0] > limit:
                left = min(max_heap[0][1],min_heap[0][1]) + 1
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)

            res = max(res,right - left + 1)

        return res