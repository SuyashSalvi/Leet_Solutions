class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        p = 0
        ans = 0

        for num in range(1,n+1):
            if p < len(banned) and banned[p] == num:
                while p < len(banned) and banned[p] == num:
                    p += 1
            else:
                maxSum -= num
                if maxSum < 0:
                    break
                ans += 1
        return ans