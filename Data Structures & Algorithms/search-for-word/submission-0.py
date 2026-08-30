class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c, index):
            if board[r][c] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            
            temp, board[r][c] = board[r][c], "#"
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if 0 <= new_row < n and 0 <= new_col < m:
                    if dfs(new_row, new_col, index + 1):
                        board[r][c] = temp
                        return True
            board[r][c] = temp
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        
        return False