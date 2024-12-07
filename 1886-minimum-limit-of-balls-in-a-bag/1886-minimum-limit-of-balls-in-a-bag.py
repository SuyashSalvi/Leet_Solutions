class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def isPossible(m, nums, maxOp):
            numOp = 0
            for num in nums:
                numOp += math.ceil(num/m) - 1
                if numOp > maxOp: return False

            return True

        l = 1
        r = max(nums)
        while l < r:
            m = (l + r) // 2
            if isPossible(m,nums,maxOperations):
                r = m 
            else:
                l = m + 1

        return l