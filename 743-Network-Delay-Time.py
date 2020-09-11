class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        visited=[False]*N
        graph={}
        d=[10000000]*N
        for u,v,w in times:
            if u not in graph:
                graph[u]=[]
            graph[u].append((v,w))
        self.ret=0
        self.total=0
        def dfs(idx,tin):
            visited[idx-1]=True
            self.total+=1
            self.ret=max(self.ret,tin)
            lst=graph.get(idx,[])
            for next,w in lst:
                if not visited[next-1]:
                    dfs(next,tin+w)
        dfs(K,0)
        if self.total!=N:
            return -1
        return self.ret