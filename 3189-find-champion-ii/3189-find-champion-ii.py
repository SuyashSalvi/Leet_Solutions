class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n

        for e in edges:
            indegree[e[1]] += 1

        champ = -1
        champ_count = 0

        for i in range(n):
            if indegree[i] == 0:
                champ = i
                champ_count += 1


        return champ if champ_count == 1 else -1