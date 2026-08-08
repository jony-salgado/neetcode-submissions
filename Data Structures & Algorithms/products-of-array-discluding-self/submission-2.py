# [1, 2, 4, 6]
# [1, 2, 8, 48]
# [48, 48, 24, 6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_to_right = []
        arr_to_left = []

        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            arr_to_right.append(product)

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            arr_to_left.append(product)

        arr_to_left = arr_to_left[::-1]

        ans = []
        for i in range(len(nums)):
            product = 1
            if i != 0:
                product *= arr_to_right[i - 1]
            if i < len(nums) - 1:
                product *= arr_to_left[i + 1]
            
            ans.append(product)

        return ans