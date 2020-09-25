class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        tin=[0]*n
        low=[0]*n
        visited=[False]*n
        self.timer=1
        graph=[[] for _ in range(n)]
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        self.ret=[]
        def dfs(node,parent):
            tin[node]=self.timer
            low[node]=self.timer
            visited[node]=True
            self.timer+=1
            for next in graph[node]:
                if visited[next]:
                    if next!=parent:
                        low[node]=min(tin[next],low[node])
                else:
                    dfs(next,node)
                    low[node]=min(low[node],low[next])
                    if tin[node]<low[next]:
                        self.ret.append([node,next])
        dfs(0,-1)
        return self.ret  
