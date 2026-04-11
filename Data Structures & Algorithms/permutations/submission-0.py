class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        remains = nums[:]
        def dfs(depth, i, subset):
            if i >= len(nums):
                i = 0
             
            subset.append(nums[i])
            if len(subset) == len(nums):
                ret.append(subset[:])
                return
                
            
            for idx in range(0, len(nums)):
                if nums[idx] in subset:
                    continue
                
                dfs(depth + 1, idx, subset)
                subset.pop()

        for i in range(0, len(nums)):
            dfs(0, i, [])
        
        return ret