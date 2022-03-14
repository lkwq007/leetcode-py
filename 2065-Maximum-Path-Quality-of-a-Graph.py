class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # There are at most four edges connected to each node.
        # test case ensure no multi-edges
        # 10 <= timej, maxTime <= 100, just brute force?
        graph=[{} for _ in range(len(values))]
        for u,v,t in edges:
            graph[u][v]=t
            graph[v][u]=t
        self.max=0
        def dfs(x,acc,rest):
            if rest<0:
                return
            cur=values[x]
            acc+=cur
            values[x]=0
            if x==0 and rest>=0:
                self.max=max(self.max,acc)
            for next in graph[x]:
                t=graph[x][next]
                if rest>=t:
                    dfs(next,acc,rest-t)
            values[x]=cur
        dfs(0,0,maxTime)
        return self.max