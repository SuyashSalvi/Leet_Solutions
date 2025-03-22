class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        extra_closing = 0
        for c in s:
            if c == '(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    extra_closing += 1

        return len(stack) + extra_closing