class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph=[{} for _ in range(n+1)]
        for u,v in paths:
            graph[u][v]=1
            graph[v][u]=1
        visited=[0]*(n+1)
        def dfs(x):
            lst=[]
            for next in graph[x]:
                if visited[next]!=0:
                    lst.append(visited[next])
            for i in range(1,5):
                if i not in lst:
                    visited[x]=i
                    break
            for next in graph[x]:
                if visited[next]==0:
                    dfs(next)
        for i in range(1,n+1):
            if visited[i]==0:
                dfs(i)
        return visited[1:]