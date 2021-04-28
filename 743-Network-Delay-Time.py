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