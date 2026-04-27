class Solution:
    def climbStairs(self, n: int) -> int:
        
        #1 or 2steps at a time
        count = 0
        dp = {}
        dp[1] = 1
        dp[2] = 2
        def climb(n):
            if n in dp:
                return dp[n]
            
            dp[n-1] = climb(n-1)
            dp[n-2] = climb(n-2)
            return dp[n-1] + dp[n-2]

        return climb(n)