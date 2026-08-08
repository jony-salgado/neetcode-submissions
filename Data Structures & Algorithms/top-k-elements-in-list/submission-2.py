from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        
        ans = []
        for key, value in frequency.items():
            ans.append((key, value))

        ans = sorted(ans, key=lambda x: x[1], reverse=True)
        ans = [key for key, _ in ans]

        return ans[:k] if k < len(ans) else ans
        