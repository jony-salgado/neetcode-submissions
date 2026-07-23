class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for j in t:
            if j not in hashmap or hashmap[j] == 0:
                return False
            hashmap[j] -= 1

        for key in hashmap:
            if hashmap[key] != 0:
                return False

        return True