from collections import Counter
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = Counter(arr)
        return any((num != 0 and 2 * num in count) or (num == 0 and count[num] > 1) for num in arr)
 