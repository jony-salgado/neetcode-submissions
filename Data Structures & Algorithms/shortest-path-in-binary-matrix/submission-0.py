class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if not grid or rows == 0 or cols == 0:
            return 0
        
        directions = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1)]

        queue = deque()
        visited = set()
        queue.append((0,0))

        ans = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == 1 or (r, c) in visited:
                    continue
                
                if r == rows - 1 and c == cols - 1:
                    return ans
                

                for dr, dc in directions:
                    visited.add((r, c))
                    queue.append((r + dr, c + dc))
            
            ans += 1
        
        return -1

