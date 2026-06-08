import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0] * 26
        for t in tasks:
            counter[ord(t) - ord('A')] += 1

        hq = []
        for c in counter:
            if c > 0:
                heapq.heappush_max(hq, c)
        
        dq = deque()
        cycle = 0
        while dq or hq:
            cycle += 1

            if hq:
                cnt = heapq.heappop_max(hq) - 1
                if cnt > 0:
                    dq.append((cnt, cycle + n))
            else:
                cycle = dq[0][1]
            
            if dq and dq[0][1] == cycle:
                heapq.heappush_max(hq, dq.popleft()[0])


        print(hq)

        return cycle
