from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_counts= Counter(s1)
        window_counts = Counter(s2[:n1])

        if s1_counts == window_counts:
            return True

        for i in range(n1, n2):

            window_counts[s2[i]] += 1

            left_letter = s2[i - n1]
            if window_counts[left_letter] == 1:
                del window_counts[left_letter]
            else:
                window_counts[left_letter] -= 1


            if window_counts == s1_counts:
                return True

        return False
