class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)

        for src, dst in prerequisites:
            adj[dst].append(src)

        visited = [0] * numCourses
        top_sort = list()

        def dfs(src, adj, visited, top_sort):
            if visited[src] == 1:
                return False
            if visited[src] == 2:
                return True

            visited[src] = 1

            for neigh in adj[src]:
                if not dfs(neigh, adj, visited, top_sort):
                    return False
            visited[src] = 2
            top_sort.append(src)
            return True

        for i in range(numCourses):
            if not dfs(i, adj, visited, top_sort):
                return []

        top_sort.reverse()
        return top_sort