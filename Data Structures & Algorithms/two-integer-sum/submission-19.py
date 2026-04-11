class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort = { i:n for i, n in enumerate(nums)}
        i = 0
        j = len(nums) - 1
        sort = dict(sorted(sort.items(), key= lambda x:x[1]))
        keys = list(sort.keys())
        #print(sort, keys)
        answer = []
        while i < j:
            sums = sort[keys[i]] + sort[keys[j]]
            #print(keys[i], sort[keys[i]], keys[j], sort[keys[j]])
            if sums == target:
                answer = [keys[i], keys[j]]
                break
            elif sums < target:
                i += 1
            else:
                j -= 1

        answer.sort()
        return answer
            
