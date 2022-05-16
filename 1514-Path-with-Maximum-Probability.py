class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        import heapq
        heap=[(-1,start)]
        graph=[{} for _ in range(n)]
        for i in range(len(edges)):
            a,b=edges[i]
            p=succProb[i]
            graph[a][b]=p
            graph[b][a]=p
        lst=[0.0]*n
        while heap:
            p,x=heapq.heappop(heap)
            p=-p
            if p<lst[x]:
                continue
            for next in graph[x]:
                tmp=p*graph[x][next]
                if tmp>lst[next]:
                    lst[next]=tmp
                    heapq.heappush(heap,(-tmp,next))
        return lst[end]