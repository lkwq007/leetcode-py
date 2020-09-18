class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # nodes inside a cyvle cannot enter the safe state
        state=[0]*len(graph)
        cycle=[False]*len(graph)
        def dfs(u):
            state[u]=1
            flag=False
            for v in graph[u]:
                if state[v]==0:
                    if dfs(v):
                        flag=True
                elif state[v]==1:
                    cycle[v]=True
                    flag=True
                else:
                    flag=cycle[v] if cycle[v] else flag
            if flag:
                cycle[u]=True
            state[u]=2
            return flag
        for i in range(len(graph)):
            if state[i]==0:
                if dfs(i):
                    cycle[i]=True
        return [i for i in range(len(graph)) if not cycle[i]]