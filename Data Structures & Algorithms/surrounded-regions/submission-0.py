class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def capture(i, j):
            if (i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != "O"):
                return
            
            board[i][j] = "T"
            capture(i, j+1)
            capture(i+1, j)
            capture(i, j-1)
            capture(i-1, j)

        #1. capture unsurrounded O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in (0, rows-1) or c in (0, cols-1)):
                    capture(r, c)
        #2. capture surrounded O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #3. Uncapture unsurrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"