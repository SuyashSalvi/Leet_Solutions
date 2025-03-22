class Solution:
    def minWindow(self, s, t):
        l, r = 0, 0
        freq_T = Counter(t)
        window_freq = {}
        formed, required = 0, len(freq_T)
        ans = float('inf'),None, None
        while r < len(s):
            ch = s[r]
            window_freq[ch] = window_freq.get(ch, 0) + 1

            if (ch in freq_T and freq_T[ch] == window_freq[ch]):
                formed += 1

            while l <= r and formed == required:
                ch = s[l]
                if r - l + 1 < ans[0]:
                    ans = r - l + 1, l, r

                window_freq[ch] -= 1
                if (ch in freq_T and window_freq[ch] < freq_T[ch]):
                    formed -= 1

                l += 1
            r += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]