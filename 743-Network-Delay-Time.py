class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        visited=[-1]*N
        graph={}
        for u,v,w in times:
            if u not in graph:
                graph[u]=[]
            graph[u].append((v,w))
        def dfs(idx,tin):
            visited[idx-1]=tin
            lst=graph.get(idx,[])
            for next,w in lst:
                if visited[next-1]==-1 or visited[next-1]>tin+w:
                    dfs(next,tin+w)
        dfs(K,0)
        for item in visited:
            if item==-1:
                return -1
        return max(visited)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        dist=[-1]*(n+1)
        graph=[[] for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append((v,w))
        dist[k]=0
        heap=[(0,k)]
        while heap:
            t,x=heapq.heappop(heap)
            if t>dist[x]:
                continue
            for next,delta in graph[x]:
                if dist[next]==-1 or delta+t<dist[next]:
                    dist[next]=delta+t
                    heapq.heappush(heap,(delta+t,next))
        acc=dist[1]
        for i in range(1,n+1):
            if dist[i]==-1:
                return -1
            acc=max(acc,dist[i])
        return acc
        