class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        template=[0]*(n+1)
        graph=[template[:] for _ in range(n+1)]
        trio=[]
        for u,v in edges:
            graph[u][v]=1
            graph[v][u]=1
        ret=-1
        acc=list(map(sum,graph))
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if graph[i][j]==1:
                    for k in range(j,n+1):
                        if graph[i][k]==1 and graph[j][k]==1:
                            if ret==-1:
                                ret=acc[i]+acc[j]+acc[k]-6
                            ret=min(acc[i]+acc[j]+acc[k]-6,ret)
        return ret