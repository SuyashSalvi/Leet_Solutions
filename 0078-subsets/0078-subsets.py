class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            res.append(path)
            for i in range(start, n):
                backtrack(i+1, path+[nums[i]])
        res = []
        n = len(nums)
        backtrack(0,[])
        return res