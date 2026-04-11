class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        arr = set(nums)
        max_count = 0
        for num in nums:
            if num-1 not in arr:
                count = 0
                for i in range(len(arr)):
                    if num+i not in arr:
                        break
                    count += 1
                
                max_count = max(count, max_count)

        return max_count
            
            
