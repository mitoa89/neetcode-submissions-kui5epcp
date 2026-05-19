class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = deque()
        remain = 1
        for i in range(len(digits) -1, -1, -1):
            tmp = digits[i] + remain
            remain = int(tmp / 10) if tmp >= 10 else 0
            ans.appendleft(tmp % 10)

        if remain > 0:
            ans.appendleft(remain)
        
        return list(ans)