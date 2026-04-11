from math import sqrt, pow

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestPoints = []
        for point in points:
            dist = sqrt(pow(point[0] - 0,2) + pow(point[1] - 0,2))
            heapq.heappush(closestPoints, (dist, point))
        
        results = []
        while len(results) < k:
            results.append(heapq.heappop(closestPoints)[1])
        return results