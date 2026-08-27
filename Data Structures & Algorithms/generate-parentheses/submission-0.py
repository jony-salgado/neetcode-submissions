class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = []
        ans = []

        def backtracking(open_, close_):
            if open_ == close_ == n:
                ans.append("".join(curr))
                return

            if open_ < n:
                curr.append("(")
                backtracking(open_ + 1, close_)
                curr.pop()
            if close_ < open_:
                curr.append(")")
                backtracking(open_, close_ + 1)
                curr.pop()

        backtracking(0, 0)
        return ans