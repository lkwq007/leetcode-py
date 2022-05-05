import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        if n==1:
            return 1
        graph=[{} for _ in range(n)]
        for u,v,t in roads:
            graph[u][v]=t
            graph[v][u]=t
        def dijkstra(x):
            dist=[-1]*n
            dist[x]=0
            heap=[(0,x)]
            while heap:
                d,cur=heapq.heappop(heap)
                if d>dist[cur]:
                    continue
                for next in graph[cur]:
                    if dist[next]==-1 or dist[cur]+graph[cur][next]<dist[next]:
                        dist[next]=dist[cur]+graph[cur][next]
                        heapq.heappush(heap,(dist[next],next))
            return dist
        lst=dijkstra(0)
        term=10**9+7
        idx=list(range(n))
        idx.sort(key=lambda x:lst[x])
        dp=[0]*n
        dp[0]=1
        for i in range(len(idx)):
            cur=idx[i]
            for next in graph[cur]:
                if lst[next]<lst[cur] and lst[next]+graph[cur][next]==lst[cur]:
                    dp[cur]+=dp[next]
                    dp[cur]%=term
            if cur==n-1:
                return dp[cur]