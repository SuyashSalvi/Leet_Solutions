class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        indegree = {i:0 for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
            
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        return order if len(order) == numCourses else []