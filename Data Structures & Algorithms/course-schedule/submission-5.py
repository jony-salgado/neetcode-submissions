from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visited = set()
        memo = {}

        def dfs(src, adj, visited):
            if src in visited:
                return False
            if src in memo:
                return memo[src]
            
            visited.add(src)

            for neigh in adj[src]:
                if not dfs(neigh, adj, visited):
                    return False
            visited.remove(src)
            memo[src] = True
            return True


        for i in range(numCourses):
            if not dfs(i, adj, visited):
                return False

        return True