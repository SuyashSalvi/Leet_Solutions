class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero_indices = []
        self.nonzero_values = []
        for i in range(len(nums)):
            if nums[i] != 0:
                self.nonzero_indices.append(i)
                self.nonzero_values.append(nums[i])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        i, j = 0, 0
        while i < len(self.nonzero_values) and j < len(vec.nonzero_values):
            idx1 = self.nonzero_indices[i]
            idx2 = vec.nonzero_indices[j]
            if idx1 == idx2:
                ans += self.nonzero_values[i] * vec.nonzero_values[j]
                i += 1
                j += 1
            elif idx1 < idx2:
                i += 1
            else:
                j += 1

        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)