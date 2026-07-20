class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        #seen = set()
        area = 0

        def dfs(i, j):
            if i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            a = 1
            a += dfs(i, j+1)
            a += dfs(i+1, j)
            a += dfs(i, j-1)
            a += dfs(i-1, j)
            return a

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        return area