class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_location = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_location == -1:
                    zero_location = i
                    continue
                else:
                    return [0] * len(nums)
            product *= nums[i]

        if zero_location == -1:
            return [int(product/nums[i]) for i in range(len(nums))]
        
        return [0 if i != zero_location else product for i in range(len(nums))]

