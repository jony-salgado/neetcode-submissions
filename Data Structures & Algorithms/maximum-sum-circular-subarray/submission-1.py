class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max = nums[0]
        global_min = nums[0]
        cur_max, cur_min, total = 0, 0, 0

        for num in nums:
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)
            total += num
            global_max = max(global_max, cur_max)
            global_min = min(global_min, cur_min)

        return max(global_max, total - global_min) if global_max > 0 else global_max