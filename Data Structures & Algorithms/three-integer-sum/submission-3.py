class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        dic = defaultdict(set)
        nums.sort()
        #for i, num in enumerate(nums):
        #    dic[num].add(i)
        # -4 -1 -1 0 1 2 
        ans = []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            diff = 0 - nums[i]
            while j < k:
                mid = nums[j] + nums[k]
                if mid == diff:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                elif mid < diff:
                    j += 1
                else:
                    k -= 1
        return ans
'''
        answer = set()
        for i in range(0, len(nums)):
            diff = 0 - nums[i]
            for j in range(i+1, len(nums)):
                diff2 = diff - nums[j]
                for k in range(j+1, len(nums)):
                    if nums[k] == diff2:
                        a = [nums[i], nums[j], nums[k]]
                        a.sort()
                        answer.add(tuple(a))
        ans = []
        for i in answer:
            ans.append(list(i))
            '''