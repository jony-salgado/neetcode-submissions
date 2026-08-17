from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for s, d, p in flights:
            if s not in graph:
                graph[s] = [(d, p)]
            else:
                graph[s].append((d, p))

        prices = [float("inf")] * n
        prices[src] = 0

        q = deque([(0, src, 0)]) # total_cost, city, stops

        while q:
            cst, node, stops = q.popleft()

            if stops > k or node not in graph:
                continue

            for nei, price in graph[node]:
                next_cost = cst + price

                if next_cost < prices[nei]:
                    prices[nei] = next_cost
                    q.append((next_cost, nei, stops + 1))

        return prices[dst] if prices[dst] != float('inf') else -1