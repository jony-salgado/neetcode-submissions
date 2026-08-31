class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        directions = [(1, 0), (0, 1)]
        def dfs(i, j, grid):
            if grid[i][j] == -1:
                return 0
            if grid[i][j] != 0:
                return grid[i][j]

            if i == m - 1 and j == n - 1:
                return 1
            
            grid[i][j] = -1
            curr = 0
            for r, c in directions:
                new_row, new_col = i + r, j + c
                if not 0 <= new_row < m or not 0 <= new_col < n:
                    continue
                
                curr += dfs(new_row, new_col, grid)
            grid[i][j] = curr
            return grid[i][j]
        
        return dfs(0, 0, grid)
