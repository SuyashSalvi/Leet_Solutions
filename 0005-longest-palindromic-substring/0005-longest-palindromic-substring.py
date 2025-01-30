class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_pallindrome = ""

        def expandAroundCenter(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(n):
            odd_pallindrome = expandAroundCenter(i, i)
            even_pallindrome = expandAroundCenter(i, i + 1)

            if len(odd_pallindrome) > len(longest_pallindrome):
                longest_pallindrome = odd_pallindrome
            if len(even_pallindrome) > len(longest_pallindrome):
                longest_pallindrome = even_pallindrome
        
        return longest_pallindrome