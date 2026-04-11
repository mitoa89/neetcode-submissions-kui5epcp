class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = set()
        # 땅 목록
        for x, g in enumerate(grid):
            for y, k in enumerate(g):
                if k == "1":
                    islands.add((x, y))
        
        if not islands:
            return 0

        def canvisit(x, y):
            if (x, y) not in islands:
                return False

            queue.append((x,y))
            islands.remove((x, y))
            return True

        count = 0
      
        while islands:
            start = islands.pop()
            queue = deque([start])

        
            while queue:
                x, y = queue.popleft()

                #왼 오 아래 갈수있는데 넣기
                canvisit(x+1, y)
                canvisit(x, y+1)
                canvisit(x-1, y)
                canvisit(x, y-1)
            count += 1
        
        return count
