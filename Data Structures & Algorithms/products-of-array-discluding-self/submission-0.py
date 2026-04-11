class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        def totalMultiply(begin, end, index):
            total = 1
            for j in range(begin, end):
                if j != index:
                    total *= nums[j]
            return total

        answer = []
        for i in range(0, len(nums)):
            answer.append(totalMultiply(0, len(nums), i))

        return answer 