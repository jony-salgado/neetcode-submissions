# [ 1, 2, 3, 4, 4, 2, 1]
#         l     r

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = num ^ ans

        return ans
