import heapq
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        def dijkstra(g,src):
            dist=[-1]*len(patience)
            heap=[(0,src)]
            dist[0]=0
            while heap:
                d,x=heapq.heappop(heap)
                if dist[x]>d:
                    continue
                for next in g[x]:
                    if dist[next]==-1 or d+1<dist[next]:
                        dist[next]=d+1
                        heapq.heappush(heap,(dist[next],next))
            return dist
        graph=[[] for _ in range(len(patience))]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        distance=dijkstra(graph,0)
        ret=0
        # print(distance)
        for i in range(1,len(patience)):
            total=distance[i]*2
            if patience[i]>=total:
                ret=max(ret,total+1)
            else:
                x=(total)//(patience[i])
                if (x)*(patience[i])<total:
                    ret=max(ret,(x)*(patience[i])+total+1)
                else:
                    ret=max(ret,(x-1)*(patience[i])+total+1)
        return ret