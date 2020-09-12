class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        visited=[False]*N
        graph={}
        d=[10000000]*N
        for u,v,w in times:
            if u not in graph:
                graph[u]=[]
            graph[u].append((v,w))
        d[K-1]=0
        queue=[K]
        while queue:
                    
        self.ret=0
        self.total=0
        if self.total!=N:
            return -1
        return self.ret