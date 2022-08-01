class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        import heapq
        def dijkstra(x):
            dist=[-1]*len(edges)
            dist[x]=0
            heap=[(0,x)]
            while heap:
                d,node=heapq.heappop(heap)
                if d!=dist[node]:
                    continue
                if edges[node]!=-1:
                    next=edges[node]
                    cur=d+1
                    if dist[next]==-1 or cur<dist[next]:
                        dist[next]=cur
                        heapq.heappush(heap,(cur,next))
            return dist
        d1=dijkstra(node1)
        d2=dijkstra(node2)
        ret=-1
        val=999999999
        for i in range(len(edges)):
            if d1[i]>=0 and d2[i]>=0:
                cur=max(d1[i],d2[i])
                if cur<val:
                    val=cur
                    ret=i
        return ret