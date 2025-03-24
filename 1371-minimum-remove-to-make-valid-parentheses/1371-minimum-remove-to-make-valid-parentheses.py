class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    indexes_to_remove.add(i)

        indexes_to_remove = indexes_to_remove.union(set(stack))
        res = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                res.append(c)
        return res