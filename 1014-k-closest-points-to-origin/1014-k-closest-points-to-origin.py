class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, ans = [], []
        for l in points:
            dist = l[0] * l[0] + l[1] * l[1]
            heapq.heappush(heap,(-dist,l))
            if len(heap) > k:
                heapq.heappop(heap)
                
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans