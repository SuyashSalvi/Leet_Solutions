class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1 << n):
            cur_ans = 0
            for j in range(n):
                if i & (1 << j):
                    cur_ans ^= nums[j]
            ans += cur_ans
        return ans