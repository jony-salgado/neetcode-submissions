class Solution:
    def __init__(self):
        self.separators = [0]

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += s
            self.separators.append(self.separators[-1] + len(s))
        
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        index = 0
        for i in self.separators[1:]:
            ans.append(s[index:i])
            index = i

        return ans