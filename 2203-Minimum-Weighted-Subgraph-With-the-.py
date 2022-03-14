import heapq
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def dijkstra(g,src):
            dist=[-1]*n
            dist[src]=0
            heap=[(0,src)]
            while heap:
                d,x=heapq.heappop(heap)
                if d!=dist[x] or x not in g:
                    continue
                for next in g[x]:
                    w=g[x][next]
                    if dist[x]+w<dist[next] or dist[next]==-1:
                        dist[next]=dist[x]+w
                        heapq.heappush(heap,(dist[next],next))
            return dist
        graph={}
        rgraph={}
        for u,v,w in edges:
            if u not in graph:
                graph[u]={}
            if v not in rgraph:
                rgraph[v]={}
            graph[u][v]=min(graph[u].get(v,w),w)
            rgraph[v][u]=min(rgraph[v].get(u,w),w)
        dist0=dijkstra(rgraph,dest)
        if dist0[src1]==-1 or dist0[src2]==-1:
            return -1
        dist1=dijkstra(graph,src1)
        dist2=dijkstra(graph,src2)
        ret=10**15
        for i in range(n):
            if dist1[i]>=0 and dist2[i]>=0 and dist0[i]>=0:
                ret=min(ret,dist1[i]+dist2[i]+dist0[i])
        return ret

import heapq
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph={}
        for u,v,w in edges:
            if v not in graph:
                graph[v]={}
            if u in graph[v]:
                graph[v][u]=min(graph[v][u],w)
            else:
                graph[v][u]=w
        heap=[(0,dest)]
        dp0=[-1]*n
        dp0[dest]=0
        while heap:
            dist,x=heapq.heappop(heap)
            if dist!=dp0[x] or x not in graph:
                continue
            for next in graph[x]:
                w=graph[x][next]
                if dp0[x]+w<dp0[next] or dp0[next]==-1:
                    dp0[next]=dp0[x]+w
                    heapq.heappush(heap,(dp0[next],next))
        if dp0[src1]==-1 or dp0[src2]==-1:
            return -1
        rgraph={}
        for v,u,w in edges:
            if v not in rgraph:
                rgraph[v]={}
            if u in rgraph[v]:
                rgraph[v][u]=min(rgraph[v][u],w)
            else:
                rgraph[v][u]=w
        visited=[0]*n
        heap=[(0,src1)]
        dp1=[-1]*n
        dp1[src1]=0
        while heap:
            dist,x=heapq.heappop(heap)
            if dist!=dp1[x] or x not in rgraph:
                continue
            for next in rgraph[x]:
                w=rgraph[x][next]
                if dp1[x]+w<dp1[next] or dp1[next]==-1:
                    dp1[next]=dp1[x]+w
                    heapq.heappush(heap,(dp1[next],next))
        heap=[(0,src2)]
        dp2=[-1]*n
        dp2[src2]=0
        while heap:
            dist,x=heapq.heappop(heap)
            if dist!=dp2[x] or x not in rgraph:
                continue
            for next in rgraph[x]:
                w=rgraph[x][next]
                if dp2[x]+w<dp2[next] or dp2[next]==-1:
                    dp2[next]=dp2[x]+w
                    heapq.heappush(heap,(dp2[next],next))
        ret=10**15
        for i in range(n):
            if dp1[i]>=0 and dp2[i]>=0 and dp0[i]>=0:
                ret=min(ret,dp1[i]+dp2[i]+dp0[i])
        return ret