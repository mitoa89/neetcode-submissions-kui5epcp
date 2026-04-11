class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #print(board[0][1])

        print(len(board))
        print(len(board[0]))
        found = False
        def dfs(x, y, subset, visited:set[(int,int)]):
            nonlocal found
            if x < 0 or y < 0 or y >= len(board[0]) or x >= len(board):
                return False
            
            if (x,y) in visited:
                return False

            subset.append(board[x][y])
            visited.append((x,y))
            
            if len(subset) == len(word):
                if "".join(subset) == word:
                    found = True
                
                print(visited, "".join(subset))
                return True

            if dfs(x+1, y, subset, visited):
                subset.pop()
                visited.remove((x+1,y))
            if dfs(x-1, y, subset, visited):
                subset.pop()
                visited.remove((x-1,y))
            if dfs(x, y+1, subset, visited):
                subset.pop()
                visited.remove((x,y+1))
            if dfs(x, y-1, subset, visited):
                subset.pop()
                visited.remove((x,y-1))
            return True

        for x in range(0, len(board)):
            for y in range(0, len(board[0])):
                dfs(x, y, [], [])

        return found
