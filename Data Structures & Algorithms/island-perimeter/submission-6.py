class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            q = deque([(r, c)])
            seen.add((r, c))
            perm = 0
            while q:
                x, y = q.popleft()
                for dr, dc in directions:
                    nr, nc = x + dr, y + dc
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0):
                        perm += 1
                    elif (nr, nc) not in seen:
                        seen.add((nr, nc))
                        q.append((nr, nc))
            return perm
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    return bfs(r, c)
        return 0

