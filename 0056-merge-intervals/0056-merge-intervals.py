class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = []
        for cur in intervals:
            if not merged or merged[-1][1] < cur[0]:
                merged.append(cur)
            else:
                merged[-1][1] = max(merged[-1][1], cur[1])

        return merged