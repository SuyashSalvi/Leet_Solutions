class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = set()
        for i, e in enumerate(edges):
            tree.add(e[0])
            tree.add(e[1])
            if i + 1 > len(tree) - 1:
                return False
        return n - 1 == len(edges)