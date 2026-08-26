class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def dfs(i):
            nonlocal cache, nums
            if i >= len(nums) or i < 0:
                return 0
            
            if cache[i] != -1:
                return cache[i]

            cache[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
            return cache[i]
        
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))
        
        return ans