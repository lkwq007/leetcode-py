class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        indegree=[0]*n
        graph={}
        for a,b in roads:
            indegree[a]+=1
            indegree[b]+=1
            if a not in graph:
                graph[a]={}
            if b not in graph:
                graph[b]={}
            graph[a][b]=1
            graph[b][a]=1
        ret=0
        for i in range(n):
            for j in range(i+1,n):
                between=1 if i in graph and j in graph[i] else 0
                ret=max(indegree[i]+indegree[j]-between,ret)
        return ret