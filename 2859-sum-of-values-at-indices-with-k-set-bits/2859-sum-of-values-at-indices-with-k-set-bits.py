class Solution:
    def count_set_bits(self,num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for i, n in enumerate(nums):
            if self.count_set_bits(i) == k:
                res += n
        return res