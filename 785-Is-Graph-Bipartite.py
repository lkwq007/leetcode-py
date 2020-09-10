class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)
        self.ret=True
        def dfs(node,val):
            if color[node]<0:
                color[node]=val
                for item in graph[node]:
                    dfs(item,1-val)
            elif color[node]!=val:
                self.ret=False
            return
        for idx in range(len(color)):
            if color[idx]<0:
                dfs(idx,0)
            if not self.ret:
                return self.ret
        return True