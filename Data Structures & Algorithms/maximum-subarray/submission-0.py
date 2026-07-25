class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cur_sum = 0
        ans = nums[0]
        for element in nums:
            cur_sum += element
            ans = max(ans, cur_sum)
            cur_sum = max(cur_sum, 0)

        return ans