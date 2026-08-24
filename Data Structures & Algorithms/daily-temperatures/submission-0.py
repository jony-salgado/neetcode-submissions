# [(38, 1), (36, 3), (35, 4)]
# [1, _, 1]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        ans = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                old_temp, i = stack.pop()
                ans[i] = idx - i
            
            stack.append((temp, idx))
        
        return ans