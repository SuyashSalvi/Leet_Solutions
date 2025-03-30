class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        heap = []
        cur_passengers = 0
        for num, start, end in trips:
            while heap and heap[0][0] <= start:
                drop, num_passengers = heapq.heappop(heap)
                cur_passengers -= num_passengers

            cur_passengers += num
            heapq.heappush(heap, (end, num))

            if cur_passengers > capacity:
                return False

        return True
