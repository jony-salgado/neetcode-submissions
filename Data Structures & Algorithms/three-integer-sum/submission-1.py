# [-4, -1, -1, 0, 1, 2]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if i > 0 and num == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_ = num + nums[l] + nums[r]
                if sum_ > 0:
                    r -= 1
                elif sum_ < 0:
                    l += 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return ans