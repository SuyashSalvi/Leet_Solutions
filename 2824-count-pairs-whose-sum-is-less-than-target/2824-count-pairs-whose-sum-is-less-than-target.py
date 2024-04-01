class Solution:
    def countPairs(self, nums: List[int], t: int) -> int:
        nums.sort()
        l, r, ans = 0, len(nums)-1, 0
        while l < r:
            if nums[l] + nums[r] < t:
                
                ans += r - l
                l += 1
            else:
                r -= 1
        return ans
        