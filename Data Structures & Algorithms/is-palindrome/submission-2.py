class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            right = s[r]
            left = s[l]
            if not self.alphaNum(right):
                r -= 1
                continue
            if not self.alphaNum(left):
                l += 1
                continue
            if right.lower() != left.lower():
                return False
            l += 1
            r -= 1
        
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))