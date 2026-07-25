class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_map = {i: [] for i in range(numCourses)}
        for source, dest in prerequisites:
            pre_map[source].append(dest)
        
        visiting = set()

        def dfs(source):
            if source in visiting:
                return False

            if pre_map[source] == []:
                return True
            
            visiting.add(source)
            for pre in pre_map[source]:
                if not dfs(pre):
                    return False
            visiting.remove(source)
            pre_map[source] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True