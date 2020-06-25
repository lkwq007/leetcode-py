class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if target==1:
            return 1.0 if len(edges)==0 else 0.0
        # note it's a undirected graph
        graph=[{} for _ in range(n+1)]
        for src,dst in edges:
            graph[src][dst]=1
            graph[dst][src]=1
        # do a bfs
        queue=[(1,1.0)]
        next=[]
        for time in range(t):
            for node,p in queue:
                for child in graph[node]:
                    if graph[node][child]==0:
                        continue
                    if child==target:
                        if time==t-1 or len(graph[child])<1:
                            return p/len(graph[node])
                        else:
                            return 0.0
                    graph[child][node]=0
                    next.append((child,p/len(graph[node])))
            queue=next
            next=[]
        return 0.0