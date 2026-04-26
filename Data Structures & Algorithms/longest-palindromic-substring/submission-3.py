class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]
        res_start = 0
        res_len = 1

        for right in range(n):
            for left in range(right, -1, -1):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True

                    curr_len = right - left + 1
                    if curr_len > res_len:
                        res_start = left
                        res_len = curr_len

        return s[res_start:res_start + res_len]
