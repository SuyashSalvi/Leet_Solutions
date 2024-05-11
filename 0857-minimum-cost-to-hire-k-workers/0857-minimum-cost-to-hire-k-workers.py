class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        """
        3 - 4
        10 - 4 *(10/3) = 4*3.33 = 13.33
        10 - 13.33
        
        3/4 - 0.75 
        1/8 - 0.125
        10/2 - 5
        10/2 - 5
        1/7 - 0.142
        
        b = 5, 5, 0.75
        max wage, temp - 4, 3
        
        """
        
        n = len(quality)
        bucket = sorted(zip(quality,wage),key=lambda x:x[0]/x[1],reverse=True)
        
        ans = 1e100
        total_quality = 0
        h = []
        
        for i in range(n):
            total_quality += bucket[i][0]
            heapq.heappush(h,-bucket[i][0])
            
            while len(h) > k:
                top = -heapq.heappop(h)
                total_quality -= top
            
            if len(h) == k:
                cost = total_quality * (bucket[i][1]/bucket[i][0])
                ans = min(ans,cost)
                
        return ans
             