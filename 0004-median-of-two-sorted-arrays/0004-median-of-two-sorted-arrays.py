class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # n, m, i, j, m1, m2 = len(nums1), len(nums2), 0, 0, 0, 0
        # for c in range((n+m)//2 + 1):
        #     m2 = m1
            
        #     if i < n and j < m:
        #         if (nums1[i] < nums2[j]):
        #             m1 = nums1[i]
        #             i += 1
        #         else:
        #             m1 = nums2[j]
        #             j += 1
        #     elif i < n:
        #         m1 = nums1[i]
        #         i += 1
        #     else:
        #         m1 = nums2[j]
        #         j+=1

        # return float(m1) if (n+m) % 2 == 1 else (float(m1)+float(m2))/2.0

        return median(sorted(nums1+nums2))