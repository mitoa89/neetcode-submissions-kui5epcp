class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        height = len(cost)
        dic = [-1] * height

        def dfs(step):
            if step >= height:
                return 0

            if dic[step] != -1:
                return dic[step]

            dic[step] = cost[step] + min(dfs(step + 1), dfs(step+2))

            return dic[step]

        
        return min(dfs(0), dfs(1))