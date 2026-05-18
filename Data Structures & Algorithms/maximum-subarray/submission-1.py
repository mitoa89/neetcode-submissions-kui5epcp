class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i, j = 0, 0

        currSum = nums[0]
        maxSum = currSum
        while i <= j and j < len(nums):
            
            if currSum < 0:
                i = j
                currSum = nums[j]
                
            if i is not j:
                currSum += nums[j]

            maxSum = max(currSum, maxSum)

            j += 1
        return maxSum
            

