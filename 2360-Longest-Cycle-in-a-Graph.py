class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        order=[]
        visited=[0]*len(edges)
        def dfs1(x):
            visited[x]=1
            if edges[x]!=-1 and visited[edges[x]]==0:
                dfs1(edges[x])
            order.append(x)
        comp=set()
        rev=[{} for _ in range(len(edges))]
        rev_edge=[-1]*len(edges)
        for i in range(len(edges)):
            if edges[i]!=-1:
                rev[edges[i]][i]=1
        def dfs2(x):
            visited[x]=1
            comp.add(x)
            for next in rev[x]:
                if visited[next]==0:
                    dfs2(next)
        for i in range(len(edges)):
            if visited[i]==0:
                dfs1(i)
        for i in range(len(edges)):
            visited[i]=0
        ret=-1
        for x in order[::-1]:
            if visited[x]==0:
                dfs2(x)
                if len(comp)>1:
                    ret=max(ret,len(comp))
                comp.clear()
        return ret
