class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        area = 0

        def dfs(i, j):
            if i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j] == 0:
                return 0

            if (i, j) in seen:
                return 0
            
            seen.add((i, j))
            area = 1
            area += dfs(i, j+1)
            area += dfs(i+1, j)
            area += dfs(i, j-1)
            area += dfs(i-1, j)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = max(area, dfs(r, c))
        return area