class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s = nums[0]
        ps = [s]
        for i in range(1,len(nums)):
            s += nums[i]
            ps.append(s)
        ans = [ps[len(nums)-1] - nums[0]]
        for i in range(1, len(nums)-1):
            res = abs(ps[i-1]-(ps[-1]-ps[i]))
            ans.append(res)
        if len(ps) > 1:
            ans.append(ps[-2])

        return ans