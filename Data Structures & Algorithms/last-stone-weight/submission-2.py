import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-weight for weight in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_y = -heapq.heappop(stones)
            stone_x = -heapq.heappop(stones)

            if stone_x != stone_y:
                heapq.heappush(stones, -(stone_y - stone_x))
        
        return -stones[0] if stones else 0