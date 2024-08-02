class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        nums1 = nums + nums
        # print(nums1)
        c = sum(nums)
        t = c - sum(nums1[0:c])
        ans = t
        # print(ans,c)
        for r in range(c,len(nums1)):

            if not nums1[r - c]:
                t -= 1
            if not nums1[r]:
                t += 1
            ans = min(ans, t)
        return ans