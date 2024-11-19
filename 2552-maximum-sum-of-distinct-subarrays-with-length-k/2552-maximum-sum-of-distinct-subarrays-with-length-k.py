class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        num_ind = {}
        beg = 0
        end = 0
        cur_sum = 0
        ans = 0

        while end < len(nums):
            cur = nums[end]
            last_occur = num_ind.get(cur, -1)
            # 1. fixing window size and repetition
            while beg <= last_occur or end - beg + 1 > k:
                cur_sum -= nums[beg]
                beg += 1
            # 2. adding curr element
            num_ind[cur] = end
            cur_sum += nums[end]
            # 3. checking if reached required window size and stire answer
            if end - beg + 1 == k:
                ans = max(ans, cur_sum)
            end += 1
        return ans
