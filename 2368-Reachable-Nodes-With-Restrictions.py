class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        visited=[0]*n
        restrict=set()
        for item in restricted:
            restrict.add(item)
        graph=[{} for _ in range(n)]
        for a,b in edges:
            graph[a][b]=1
            graph[b][a]=1
        def dfs(x):
            visited[x]=1
            if x in restrict:
                return 0
            acc=1
            for next in graph[x]:
                if visited[next]==0:
                    acc+=dfs(next)
            return acc
        return dfs(0)
