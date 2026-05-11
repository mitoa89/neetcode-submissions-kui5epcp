class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr = []

        i,j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        if i < len(nums1):
            arr = arr + nums1[i:]
        if j < len(nums2):
            arr = arr + nums2[j:]

        if len(arr) % 2 == 0:
            mid = len(arr)//2
            return (arr[mid] + arr[mid-1])/2
        

        return arr[len(arr)//2]