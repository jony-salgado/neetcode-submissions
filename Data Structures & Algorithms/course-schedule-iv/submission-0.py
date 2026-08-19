class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = collections.defaultdict(list)
        for dest, src in prerequisites:
            adj[src].append(dest)

        def dfs(src):
            if src not in pre_req_map:
                pre_req_map[src] = set()
                for neigh in adj[src]:
                    pre_req_map[src].update(dfs(neigh))
                pre_req_map[src].add(src)
            return pre_req_map[src]

        pre_req_map = {}
        for src in range(numCourses):
            dfs(src)

        ans = []
        for u, v in queries:
            ans.append(u in pre_req_map[v])
        return ans