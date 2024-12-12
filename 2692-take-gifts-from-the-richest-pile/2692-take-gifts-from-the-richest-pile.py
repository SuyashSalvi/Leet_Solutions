class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = [-g for g in gifts]
        res = 0
        heapq.heapify(pq)

        for _ in range(k):
            cur = -heapq.heappop(pq)
            heapq.heappush(pq, -math.floor(math.sqrt(cur)))

        while pq:
            res -= heapq.heappop(pq)

        return res
