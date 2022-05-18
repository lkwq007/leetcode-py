class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        term=10**9+7
        graph=[{} for _ in range(n+1)]
        for u,v,w in edges:
            graph[u][v]=w
            graph[v][u]=w
        import heapq
        def dijkstra(x):
            dist=[-1]*(n+1)
            dist[x]=0
            heap=[(0,x)]
            while heap:
                d,node=heapq.heappop(heap)
                if d!=dist[node]:
                    continue
                for next in graph[node]:
                    cur=d+graph[node][next]
                    if dist[next]==-1 or cur<dist[next]:
                        dist[next]=cur
                        heapq.heappush(heap,(cur,next))
            return dist
        lst=dijkstra(n)
        dp=[0]*(n+1)
        dp[1]=1
        queue=[(-lst[1],1)]
        record={}
        record[1]=1
        while queue:
            d,node=heapq.heappop(queue)
            d=-d
            for next in graph[node]:
                if lst[next]<d:
                    dp[next]=(dp[next]+dp[node])%term
                    if next not in record:
                        heapq.heappush(queue,(-lst[next],next))
                        record[next]=1
        return dp[n]