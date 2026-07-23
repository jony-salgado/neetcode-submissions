class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
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

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [0] * n
        prefix = [0] * n
        postfix = [0] * n

        prefix[0] = postfix[n-1] = 1
        for i in range(1, n):
            prefix[i] = nums[i -1] * prefix[i-1]
        for i in range(n-2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i+1]
        for i in range(n):
            ans[i] = prefix[i] * postfix[i]

        return ans