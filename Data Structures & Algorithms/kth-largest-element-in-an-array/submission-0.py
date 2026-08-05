import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return None

        heap = []
        for element in nums:
            heapq.heappush(heap, element)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]