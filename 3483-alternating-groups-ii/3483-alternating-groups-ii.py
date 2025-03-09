class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k-1):
            colors.append(colors[i])
        left, right = 0, 1
        res = 0
        while right < len(colors):
            if colors[right] == colors[right - 1]:
                left = right
                right += 1
                continue

            right += 1
            if right - left < k:
                continue

            res += 1
            left += 1

        return res