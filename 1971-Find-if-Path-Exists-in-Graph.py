class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph=[[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[0]*n
        def dfs(x):
            visited[x]=1
            if x==end:
                return True
            for next in graph[x]:
                if visited[next]==0:
                    if dfs(next):
                        return True
            return False
        return dfs(start)