class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.ret=10**12
        visited=[0]*n
        graph=[{} for _ in range(n)]
        for u,v,t in roads:
            graph[u-1][v-1]=t
            graph[v-1][u-1]=t
        def dfs(x):
            visited[x]=1
            for next in graph[x]:
                self.ret=min(self.ret,graph[x][next])
                if visited[next]==0:
                    visited[next]=1
                    dfs(next)
        dfs(0)
        return self.ret