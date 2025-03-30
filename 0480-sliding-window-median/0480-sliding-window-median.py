import heapq
from typing import List

class DualHeap:
    def __init__(self, k: int):
        self.small = []  # Max-heap (store negatives)
        self.large = []  # Min-heap
        self.delayed = {}  # {num: count} for lazy deletions
        self.k = k
        self.smallSize = 0  # effective size of small heap
        self.largeSize = 0  # effective size of large heap

    def prune(self, heap):
        # Remove the top of the heap if it is scheduled for deletion.
        while heap:
            num = -heap[0] if heap is self.small else heap[0]
            if num in self.delayed and self.delayed[num] > 0:
                heapq.heappop(heap)
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    del self.delayed[num]
            else:
                break

    def balance(self):
        # Ensure the sizes satisfy: smallSize == largeSize or smallSize == largeSize + 1
        if self.smallSize > self.largeSize + 1:
            # Move the top element from small to large
            num = -heapq.heappop(self.small)
            self.smallSize -= 1
            heapq.heappush(self.large, num)
            self.largeSize += 1
            self.prune(self.small)
        elif self.smallSize < self.largeSize:
            # Move the top element from large to small
            num = heapq.heappop(self.large)
            self.largeSize -= 1
            heapq.heappush(self.small, -num)
            self.smallSize += 1
            self.prune(self.large)

    def add(self, num: int):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.smallSize += 1
        else:
            heapq.heappush(self.large, num)
            self.largeSize += 1
        self.balance()

    def remove(self, num: int):
        # Mark num as delayed for removal.
        self.delayed[num] = self.delayed.get(num, 0) + 1
        if num <= -self.small[0]:
            self.smallSize -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.largeSize -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.balance()

    def get_median(self) -> float:
        if self.k % 2 == 1:
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        res = []
        
        # Initialize the dual heap with the first k elements.
        for i in range(k):
            dh.add(nums[i])
        res.append(dh.get_median())
        
        # Process the remaining elements.
        for i in range(k, len(nums)):
            dh.add(nums[i])
            dh.remove(nums[i - k])
            res.append(dh.get_median())
        
        return res