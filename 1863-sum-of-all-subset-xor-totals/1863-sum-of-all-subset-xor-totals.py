class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(ind, cur_ans):
            if ind == len(nums):
                return cur_ans
            incl = dfs(ind + 1, cur_ans^nums[ind])
            excl = dfs(ind + 1, cur_ans)
            return incl + excl
        return dfs(0,0)