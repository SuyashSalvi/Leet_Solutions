class Solution:
    def dfs(self, i, adj, inStack, visited):
        if inStack[i]:
            return True
        if visited[i]:
            return False
        visited[i] = True
        inStack[i] = True
        for neigh in adj[i]:
            if self.dfs(neigh, adj, inStack, visited):
                return True
        inStack[i] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])

        visited = [False] * numCourses
        inStack = [False] * numCourses

        for i in range(numCourses):
            if self.dfs(i, adj, inStack, visited):
                return False
        return True