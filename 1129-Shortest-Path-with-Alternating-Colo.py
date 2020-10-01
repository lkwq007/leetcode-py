class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_graph=[[] for i in range(n)]
        blue_graph=[[] for i in range(n)]
        for u,v in red_edges:
            red_graph[u].append(v)
        for u,v in blue_edges:
            blue_graph[u].append(v)
        graph=[red_graph,blue_graph]
        red=[-1]*n
        red[0]=0
        blue=red[:]
        visited=[red,blue]
        queue=[(0,0),(0,1)]
        ret=[-1]*n
        ret[0]=0
        step=0
        while queue:
            target=[]
            step+=1
            for u,state in queue:
                for v in graph[1-state][u]:
                    if visited[1-state][v]==-1:
                        visited[1-state][v]=step
                        if ret[v]==-1:
                            ret[v]=step
                        else:
                            ret[v]=min(ret[v],step)
                        target.append((v,1-state))
            queue=target
        return ret