class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs_sum(index, sum, subset: List[int]):
            if sum > target:
                return

            print(f"sum {sum} subset {subset}")

            if sum == target:
                res.append(subset[:])
                return
                
            for i in range(index, len(nums)):
                subset.append(nums[i])
                dfs_sum(i, sum + nums[i], subset)
                subset.pop()

        dfs_sum(0, 0, [])

        return res
