#brute force: iterate through all 1, n-1 and calculate the amount of water at that point by {max(0, min(left_max,right_max) - height)} => O(n^2)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        leftMax, rightMax = 0, 0
        total_water = 0
        
        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                total_water += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                total_water += rightMax - height[right]
                right -= 1
        return total_water