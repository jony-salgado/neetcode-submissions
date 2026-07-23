class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if len(image) == 0 or len(image[0]) == 0:
            return image

        init_color = image[sr][sc]
        if init_color == color:
            return image
            
        visited = set()
        self.dfs(image, sr, sc, init_color, color, visited)
        return image
    
    def dfs(self, image: List[List[int]], r:int, c:int, init_color:int, color:int, visited:set[tuple[int]]):
        
        if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
            return
        if (r, c) in visited or image[r][c] != init_color:
            return

        visited.add((r, c))
        image[r][c] = color

        self.dfs(image, r+1, c, init_color, color, visited)
        self.dfs(image, r-1, c, init_color, color, visited)
        self.dfs(image, r, c+1, init_color, color, visited)
        self.dfs(image, r, c-1, init_color, color, visited)
        


