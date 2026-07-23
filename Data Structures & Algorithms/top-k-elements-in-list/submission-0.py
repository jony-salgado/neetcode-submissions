class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        table = dict()

        for num in nums:
            table[num] = table.get(num, 0) + 1
        
        freq = []
        for key, value in table.items():
            freq.append([key, value])
        
        freq.sort(key=lambda a: a[1], reverse=True)

        return [element[0] for element in freq[:k]]