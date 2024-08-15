from collections import Counter

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        cur = {5:0,10:0,20:0}
        for b in bills:
            if b == 5:
                cur[5] += 1
            elif b == 10:
                if cur[5] > 0:
                    cur[5] -= 1
                    cur[10] += 1
                else:
                    return False
            else:
                if cur[10] > 0 and cur[5]>0:
                    cur[10] -= 1
                    cur[5] -= 1
                elif cur[5] > 2:
                    cur[5] -= 3
                else: 
                    return False
        return True