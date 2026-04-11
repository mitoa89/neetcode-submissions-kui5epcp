class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            #정렬되어있는 쪽에 포함되어있는지?
            #아니라면 반대임
            #정렬된 데 찾기?
            if nums[left] <= nums[mid]: #왼쪽이 정렬된 상태
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if  nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        return -1