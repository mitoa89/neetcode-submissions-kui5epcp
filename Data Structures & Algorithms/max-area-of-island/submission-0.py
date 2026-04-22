class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width = len(grid)
        length = len(grid[0])

        islands = {}
        visited = set()
        queue = deque()

        def visit(i,j):
            if i < 0 or j < 0 or i >= width or j >= length:
                return
            if (i,j) in visited:
                return
            if grid[i][j] == 0:
                return
            visited.add((i, j))
            queue.append((i, j))

        max_area = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (i,j) in visited:
                    continue
                if grid[i][j] == 0:
                    continue
                    
                visit(i, j)
                
                area = 0
                while queue:
                    (x, y) = queue.popleft()
                    area += 1

                    #print(i, j, x, y, area)
                    visit(x-1, y)
                    visit(x, y-1)
                    visit(x+1, y)
                    visit(x, y+1)
                
                max_area = max(area, max_area)

        return max_area