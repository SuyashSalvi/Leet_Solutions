class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = sum(nums)
        ans = [n]
        for i in range(len(nums)-1,0,-1):
            n -= nums[i]
            ans.append(n)
        return ans[::-1]