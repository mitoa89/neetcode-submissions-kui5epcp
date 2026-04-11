class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def make(strs):
            if not strs:
                return 0
            if len(strs) == 1:
                return strs[0]

            dp = [0] * len(strs)
            dp[0] = strs[0]
            dp[1] = max(strs[0], strs[1])

            # [rob1, rob2, n, ...]
            for n in range(2, len(strs)):
                dp[n] = max(strs[n] + dp[n-2], dp[n-1])

            return dp[-1]

        dp1 = make(nums[:-1])
        dp2 = make(nums[1:])

    
        return max(dp1, dp2)