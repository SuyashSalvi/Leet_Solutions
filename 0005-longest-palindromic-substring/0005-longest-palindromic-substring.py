class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Transform string to handle even-length palindromes uniformly
        T = "#".join(f"^{s}$")  # Example: "babad" -> "^#b#a#b#a#d#$"
        n = len(T)
        P = [0] * n
        center = right = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i  # Mirror of i with respect to center

            if i < right:
                P[i] = min(right - i, P[mirror])  # Use previously computed palindrome lengths

            # Expand around center
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1

            # Update center and right boundary
            if i + P[i] > right:
                center, right = i, i + P[i]

        # Find the maximum length palindrome
        max_len, center_index = max((P[i], i) for i in range(1, n - 1))
        start = (center_index - max_len) // 2  # Convert index back to original string
        return s[start: start + max_len]