class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtracking(i, curr):
            if i >= len(nums):
                if curr[:] not in ans:
                    ans.append(curr[:])
                return

            curr.append(nums[i])
            backtracking(i+1, curr)
            curr.pop()
            backtracking(i+1, curr)
        

        backtracking(0, [])
        return ans