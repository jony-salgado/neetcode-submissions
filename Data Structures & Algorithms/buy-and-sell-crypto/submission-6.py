# [2, 1, 2, 1, 0, 1, 2]
#           l     r
# ans = 1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        ans = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                curr = prices[r] - prices[l]
                ans = max(ans, curr)
            else:
                l = r
            
            r += 1

        return ans