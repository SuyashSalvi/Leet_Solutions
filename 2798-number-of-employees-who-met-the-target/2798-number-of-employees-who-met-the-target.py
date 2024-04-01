class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        n = len(hours)
        for i in range(n-1,-1,-1):
            if hours[i]<target:
                return n-i-1
        return n