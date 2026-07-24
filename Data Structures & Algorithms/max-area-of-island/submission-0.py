class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if not grid or rows == 0 or cols == 0:
            return 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(r, c):
            if r >= rows or c >= cols or min(r, c) < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    ans = max(area, ans)
        
        return ans