from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        n1, n2 = len(s), len(t)

        if n1 < n2:
            return ""

        t_counter = Counter(t)
        curr_counter = Counter()

        have, need = 0, len(t_counter)
        ans = ""
        l = 0
        for i in range(n1):
            c = s[i]
            if c in t_counter:
                curr_counter[c] += 1
                if curr_counter[c] == t_counter[c]:
                    have += 1

            while have == need:
                sub = s[l:i+1]
                if ans == "" or len(sub) < len(ans):
                    ans = sub

                left_char = s[l]
                if left_char in t_counter:
                    if curr_counter[left_char] == t_counter[left_char]:
                        have -= 1
                    curr_counter[left_char] -= 1
                
                l += 1

        return ans

             