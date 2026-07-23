class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s)%2 == 1:
            return False
        map_ = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        for i in range(len(s)):
            if s[i] in ['{', '(', '[']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                element = stack.pop()
                if element != map_[s[i]]:
                    return False

        return True if len(stack) == 0 else False
                
