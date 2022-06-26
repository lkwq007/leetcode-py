class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        ret=0
        val=0
        for item in nums:
            val^=item
        ret=99999999999
        degree=[0]*len(nums)
        graph=[{} for _ in range(len(nums))]
        edge=[{} for _ in range(len(nums))]
        for u,v in edges:
            degree[u]+=1
            degree[v]+=1
            graph[u][v]=1
            graph[v][u]=1
        for i in range(len(nums)):
            if degree[i]==1:
                idx=i
                break
        total=set(range(len(nums)))
        def dfs(x,parent):
            acc=0
            lst=set([])
            for next in graph[x].keys():
                if next!=parent:
                    cur,tmp=dfs(next,x)
                    graph[x][next]=graph[next][x]^val
                    edge[x][next]=total-tmp
                    acc^=cur
                    lst=lst.union(tmp)
            acc^=nums[x]
            lst.add(x)
            if parent!=-1:
                graph[x][parent]=acc
                edge[x][parent]=lst
            return acc,lst
        dfs(idx,-1)
        for i in range(len(edges)):
            for j in range(i+1,len(edges)):
                a,b=edges[i]
                u,v=edges[j]
                lst=[]
                # start as set
                if a in edge[u][v]:
                    # v - (a,b,u)
                    if u in edge[a][b]:
                        v0=graph[b][a]
                        v1=graph[v][u]
                    else:
                        v0=graph[a][b]
                        v1=graph[v][u]
                else:
                    # u - (a,b,v)
                    v1=graph[u][v]
                    if v in edge[a][b]:
                        v0=graph[b][a]
                    else:
                        v0=graph[a][b]
                lst=[v0,v1,v0^v1^val]
                diff=max(lst)-min(lst)
                ret=min(ret,diff)
        return ret