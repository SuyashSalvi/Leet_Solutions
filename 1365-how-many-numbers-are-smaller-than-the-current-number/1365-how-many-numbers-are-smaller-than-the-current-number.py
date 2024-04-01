class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        prefix_count = {}
        total_count = 0
        for num in sorted(counts.keys()):
            prefix_count[num] = total_count
            total_count += counts[num]
        return [prefix_count[num] for num in nums]