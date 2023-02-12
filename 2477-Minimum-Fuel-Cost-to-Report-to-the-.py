class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n=len(roads)+1
        graph=[{} for _ in range(n)]
        for u,v in roads:
            graph[u][v]=1
            graph[v][u]=1
        # postorder
        def dfs(x,p):
            keys=list(graph[x].keys())
            if len(keys)==0:
                return 0,0,1
            ret,cnt,rest=0,0,0
            for child in keys:
                if child==p:
                    continue
                acc=dfs(child,x)
                ret+=acc[0]+acc[1]
                if acc[2]>0:
                    ret+=1
                cnt+=acc[1]
                rest+=acc[2]
            rest+=1
            cnt+=rest//seats
            rest%=seats
            return ret,cnt,rest
        return dfs(0,-1)[0]