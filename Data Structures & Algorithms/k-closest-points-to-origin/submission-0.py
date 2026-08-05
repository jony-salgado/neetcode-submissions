import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_dist = [([x, y], (x**2 + y**2)**(1/2)) for (x, y) in points]
        smallest = heapq.nsmallest(k, points_dist, key=lambda x: x[1])

        return [point for point, _ in smallest]