class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [0, 0]

        hashmap = {}

        for i in range(len(nums)):
            hashmap[target - nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in hashmap and i != hashmap[nums[i]]:
                index = [i, hashmap[nums[i]]]
                index.sort()
                return index