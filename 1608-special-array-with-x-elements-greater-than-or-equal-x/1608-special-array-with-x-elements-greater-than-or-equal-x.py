class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        nums = 5,3
        x - 0, 1, 2
        x = 0: 0<= 2and 5<0
        x = 1: 1<=2 and 3<1
        x = 2: 2<=2 and 2==2 return 2 (3 >= 2)
        """
        nums.sort(reverse=True)  # Sort in descending order

        for x in range(len(nums) + 1):
            if x <= len(nums) and (x == len(nums) or nums[x] < x):
                return x if (x == 0 or nums[x - 1] >= x) else -1

        return -1