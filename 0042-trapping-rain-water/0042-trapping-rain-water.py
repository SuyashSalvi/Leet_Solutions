#brute force: iterate through all 1, n-1 and calculate the amount of water at that point by {max(0, min(left_max,right_max) - height)} => O(n^2)

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = 0, 0
        ans = 0
        while l < r:
            if height[l] < height[r]:
                lMax = max(lMax, height[l])
                ans += lMax - height[l]
                l += 1
            else:
                rMax = max(rMax, height[r])
                ans += rMax - height[r]
                r -= 1

        return ans