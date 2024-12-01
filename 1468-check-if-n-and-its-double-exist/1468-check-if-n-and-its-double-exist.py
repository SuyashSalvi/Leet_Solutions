from collections import Counter
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        return any((num != 0 and 2 * num in Counter(arr)) or (num == 0 and Counter(arr)[num] > 1) for num in arr)
 