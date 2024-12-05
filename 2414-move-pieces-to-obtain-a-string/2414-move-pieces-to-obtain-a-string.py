class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        s, t = 0, 0

        while s < n or t < n:
            while s < n and start[s] == "_":
                s += 1
            while t < n and target[t] == "_":
                t += 1

            if s == n or t == n:
                return (s == n and t == n)

            if (start[s] != target[t] or (start[s] == "L" and s < t) or (start[s] == "R" and s > t)):
                return False

            s += 1
            t += 1
        return True