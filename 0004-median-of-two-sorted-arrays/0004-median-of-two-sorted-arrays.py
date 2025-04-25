class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        # Binary search on partition of nums1
        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            # Get border values or infinities when partition is at an end
            maxLeftA = (float('-inf') if partitionA == 0 else nums1[partitionA - 1])
            maxLeftB = (float('-inf') if partitionB == 0 else nums2[partitionB - 1])
            minRightA = (float('inf') if partitionA == m else nums1[partitionA])
            minRightB = (float('inf') if partitionB == n else nums2[partitionB])

            # Check if we have a valid partition
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                # If total length is even, median is average of max left and min right
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                # If odd, median is the max of left halves
                else:
                    return max(maxLeftA, maxLeftB)
            # If maxleftA is big, move partitionA left        
            elif maxLeftA > minRightB:
                right = partitionA - 1
            # Otherwise move partitionA right
            else:
                left = partitionA + 1