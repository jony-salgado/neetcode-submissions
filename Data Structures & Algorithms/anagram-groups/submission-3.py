from collections import defaultdict

class Solution:
    def get_index(self, letter: str) -> int:
        return ord(letter) - ord('a')

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            frequencies = [0] * 26
            for letter in string:
                frequencies[self.get_index(letter)] += 1
            

            hashmap[tuple(frequencies)].append(string)

        ans = []
        for value in hashmap.values():
            ans.append(value)

        return ans
            