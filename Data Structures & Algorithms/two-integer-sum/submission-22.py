class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        i, j = 0, len(nums) - 1

        dic = { val:i for i, val in enumerate(nums)}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic and dic[diff] != i:
                return [i, dic[diff]]
        
        return []
            
            
            
