class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(curr, pick):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for i, num in enumerate(nums):
                if not pick[i]:
                    curr.append(num)
                    pick[i] = True
                    backtrack(curr, pick)
                    curr.pop()
                    pick[i] = False

        backtrack([], [False] * len(nums))
        return ans