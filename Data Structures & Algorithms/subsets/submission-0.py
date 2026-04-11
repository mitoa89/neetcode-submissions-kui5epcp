class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        for i in range(0, 2 ** len(nums)):
            element = []
            for index in range(0, len(nums)):
                if i & (2 ** index):
                    element.append(nums[index])
            result.append(element)
        return result