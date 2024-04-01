class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = sorted(nums)
        ans = []
        for i in nums:
            ans.append(c.index(i))
        return ans