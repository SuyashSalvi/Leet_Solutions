class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return max([
            y-x
            for x,y in pairwise(sorted(p[0] for p in points))
        ])