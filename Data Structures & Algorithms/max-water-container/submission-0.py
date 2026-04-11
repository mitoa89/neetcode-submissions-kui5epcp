class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #직관을 이용할것
        #brute force한 후에 최적화해볼것
        #자료구조들 대입해볼것

        i, j = 0, len(heights) - 1
        max_amount = 0
        for i, a in enumerate(heights):
            for j in range(len(heights)-1, i, -1):
                distance = j - i
                #if k > a: #물 높이가 낮아짐

                #distance가 점점 작아지는데 a보다 크지 않는 이상 볼 필요가 없지 않나?
                k = heights[j]
                amount = min(a, k) * distance
                max_amount = max(amount, max_amount)
                #print(distance, amount, a, k)

        return max_amount