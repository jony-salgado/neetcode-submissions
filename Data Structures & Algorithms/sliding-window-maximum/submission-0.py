from collections import defaultdict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums)]

        n = len(nums)
        window = defaultdict(int)

        for i in range(k):
            window[nums[i]] += 1
        
        ans = [max(window)]

        for i in range(k, n):
            left = nums[i - k]

            if window[left] > 1:
                window[left] -= 1
            else:
                del window[left]

            window[nums[i]] += 1

            ans.append(max(window))

        return ans