class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        ans, cur = 0, 0
        while l < r:
            if heights[l] < heights[r]:
                cur = heights[l] * (r - l)
                l += 1
            else:
                cur = heights[r] * (r - l)
                r -= 1
            ans = max(ans, cur)
        
        return ans