import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)

        # minheap for chairs
        avaC = list(range(n))
        heapq.heapify(avaC)

        # minheap for arrival time
        arr = [ (times[i][0],i) for i in range(n)]
        arr.sort()

        leaQ = []

        for arrTime, fInd in arr:
            while leaQ and leaQ[0][0] <=arrTime:
                heapq.heappush(avaC, heapq.heappop(leaQ)[1])

            chair = heapq.heappop(avaC)

            if fInd == targetFriend:
                return chair
            
            heapq.heappush(leaQ, (times[fInd][1],chair))
        
        return -1