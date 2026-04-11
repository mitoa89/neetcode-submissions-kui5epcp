class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()
        def dfs(i, subset, sum):
            
            print(f"sum {sum} subset{subset}")
            if sum == target:
                result.append(subset[:])
                return

            for index in range(i, len(candidates)):
                if index > i and candidates[index] == candidates[index-1]:
                    continue
                if sum + candidates[index] > target:
                    break
            
                subset.append(candidates[index])
                dfs(index + 1, subset, sum + candidates[index])
                subset.pop()
            return
        
        dfs(0, [], 0)
        return result
