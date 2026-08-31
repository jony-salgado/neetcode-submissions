class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, part = [], []

        def dfs(j, i):
            if i >=len(s):
                if i == j:
                    ans.append(part.copy())
                return
            
            if self.is_palindrome(s, j, i):
                part.append(s[j:i+1])
                dfs(i+1, i+1)
                part.pop()
            dfs(j, i+1)

        dfs(0, 0)
        return ans

    def is_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True






