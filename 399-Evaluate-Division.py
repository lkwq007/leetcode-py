class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}
        visited={}
        for i in range(len(equations)):
            a,b=equations[i]
            val=values[i]
            if a not in graph:
                graph[a]={}
            if b not in graph:
                graph[b]={}
            graph[a][b]=val
            graph[b][a]=1.0/val
            visited[a]=False
            visited[b]=False
        ret=[-1]*len(queries)
        def dfs(node,target,acc):
            if node==target:
                return acc
            visited[node]=True
            for key in graph[node]:
                if not visited[key]:
                    tmp=dfs(key,target,acc*graph[node][key])
                    if tmp>0:
                        visited[node]=False
                        return tmp
            visited[node]=False
            return -1
        for i in range(len(queries)):
            a,b=queries[i]
            if a in graph and b in graph:
                ret[i]=dfs(a,b,1.0)
        return ret