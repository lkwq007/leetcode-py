class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        ret=[-1]*len(edges)
        visited=[-1]*len(edges)
        def dfs(u):
            v=edges[u]
            if ret[v]!=-1:
                val=ret[v]+visited[u]+1
                cycle=0
            elif visited[v]==-1:
                visited[v]=visited[u]+1
                val,cycle=dfs(v)
            else:
                cycle=visited[u]-visited[v]+1
                val=visited[u]+1
            if val-cycle>=visited[u]:
                ret[u]=val-visited[u]
            else:
                ret[u]=cycle
            return val,cycle
        for i in range(len(edges)):
            if visited[i]==-1:
                visited[i]=0
                dfs(i)
        return ret