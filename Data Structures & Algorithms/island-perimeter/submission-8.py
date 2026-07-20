class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            
            if (i, j) in seen:
                return 0
            
            seen.add((i, j))
            per = dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1) + dfs(i-1, j)
            return per

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    return dfs(r, c)
        return 0