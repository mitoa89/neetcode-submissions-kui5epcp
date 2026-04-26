class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        dic = defaultdict(int)
        res = 0
        for num in nums:
            if not dic[num]:
                dic[num] = dic[num-1] + dic[num+1] + 1
                dic[num - dic[num-1]] = dic[num]
                dic[num + dic[num+1]] = dic[num]
                res = max(res, dic[num])

        print(dic)
        return res


            