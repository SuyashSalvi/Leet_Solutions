class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = 0
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        for i in range(len(nums)-1):
            if 2 * prefix_sum[i] >= prefix_sum[-1]:
                res += 1

        return res