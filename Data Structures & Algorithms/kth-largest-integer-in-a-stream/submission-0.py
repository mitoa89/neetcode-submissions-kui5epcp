from heapq import heapify, heappush, nlargest
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:]
        heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        return nlargest(self.k, self.heap)[-1]
