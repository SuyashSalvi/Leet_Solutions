class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left_sum = [0] * n
        left_sum[0] = nums[0]
        for i in range(1,n):
            left_sum[i] = left_sum[i-1] + nums[i]
            
        right_sum = [0] * n
        right_sum[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            right_sum[i] = right_sum[i+1] + nums[i]
        ans = []
        for i in range(n):
            left = 0 if i == 0 else left_sum[i-1]
            right = 0 if i == n-1 else right_sum[i+1]
            ans.append(abs(left-right))
        return ans