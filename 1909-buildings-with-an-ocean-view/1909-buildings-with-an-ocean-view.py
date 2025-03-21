class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        # monotonically decreasing stack
        stack = []
        res = []
        for current in reversed(range(n)):
            # checking for buildings with greater height are present
            while stack and heights[stack[-1]] < heights[current]:
                stack.pop()
            # stack empty means no view block
            if not stack:
                res.append(current)

            stack.append(current)

        res.reverse()
        return res