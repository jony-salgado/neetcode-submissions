from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        ans = 0
        max_frequency = 0

        for r in range(len(s)):
            count[s[r]] += 1
            max_frequency = max(max_frequency, count[s[r]])

            if (r - l + 1) - max_frequency > k:
                count[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans

                