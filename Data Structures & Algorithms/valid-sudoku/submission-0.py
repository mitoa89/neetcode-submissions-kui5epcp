class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i:set() for i in range(0,len(board))}
        col = {i:set() for i in range(0,len(board))}
        box = {i:set() for i in range(0,len(board))}

        def getBoxNum(x, y):
            return x // 3 + (y // 3)*3

        for x in range(0, len(board)):
            for y in range(0, len(board)):
                val = board[x][y]
                if val != ".":
                    if val in row[x]:
                        return False
                    row[x].add(val)
                    if val in col[y]:
                        return False
                    col[y].add(val)
                    if val in box[getBoxNum(x, y)]:
                        return False
                    box[getBoxNum(x, y)].add(val)
        return True