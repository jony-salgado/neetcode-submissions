class Solution:
    def areAnagrams(self, t: str, r: str) -> bool:
        if len(t) != len(r):
            return False

        letters = [0] * 26

        for i in t:
            index = ord(i) - ord('a')
            letters[index] += 1

        for i in r:
            index = ord(i) - ord('a')
            letters[index] -= 1
            if letters[index] < 0:
                return False
        
        return sum(letters) == 0
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found_anagrams = set()
        ans = []
        for i, candidate in enumerate(strs):
            if candidate in found_anagrams:
                continue
            anagrans = [candidate]
            found_anagrams.add(candidate)
            for j in range(i + 1, len(strs)):
                if self.areAnagrams(candidate, strs[j]):
                    anagrans.append(strs[j])
                    found_anagrams.add(strs[j])
            
            ans.append(anagrans)
        
        return ans