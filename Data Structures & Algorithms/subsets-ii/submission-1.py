class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtracking(i, curr):
            if i == len(nums):
                ans.append(curr[:])
                return


            curr.append(nums[i])
            backtracking(i+1, curr)
            curr.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtracking(i+1, curr)
        

        backtracking(0, [])
        return ans