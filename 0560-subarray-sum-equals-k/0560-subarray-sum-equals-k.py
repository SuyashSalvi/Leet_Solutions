class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:      
        n = len(nums)  
        hm = {0:1}
        prefix_sum = 0
        ans = 0

        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum - k in hm:
                ans += hm[prefix_sum - k]
            hm[prefix_sum] = hm.get(prefix_sum, 0) + 1

        return ans