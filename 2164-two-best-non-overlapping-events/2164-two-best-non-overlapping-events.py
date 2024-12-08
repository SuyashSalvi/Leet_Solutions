class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        pq = []
        events.sort(key=lambda x: x[0])

        max_val, max_sum = 0, 0

        for event in events:

            while pq and pq[0][0] < event[0]:
                max_val = max(max_val, pq[0][1])
                heapq.heappop(pq)

            max_sum = max(max_sum, max_val + event[2])
            heapq.heappush(pq,(event[1],event[2]))

        return max_sum