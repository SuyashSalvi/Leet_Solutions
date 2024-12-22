class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = []
        cur_time, chef_idle = 0, 0
        for a, t in customers:
            cur_time = a
            res.append(max(a, chef_idle)+ t - a)
            chef_idle = max(a, chef_idle) + t

        return sum(res)/len(customers)

            