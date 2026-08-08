class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        curr_chars = set()
        l = 0
        ans = 0

        for r in range(len(s)):

            while s[r] in curr_chars:
                curr_chars.remove(s[l])
                l += 1
            
            curr_chars.add(s[r])
            ans = max(ans, r - l + 1)
        

        return ans

