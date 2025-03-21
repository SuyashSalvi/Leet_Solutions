class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        cur_tallest = 0
        res = []
        n = len(heights)
        for i in range(n-1, -1, -1):
            if heights[i] > cur_tallest:
                res.append(i)
                cur_tallest = heights[i]

        return res[::-1]