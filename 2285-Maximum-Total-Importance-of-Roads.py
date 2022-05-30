class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree=[0]*n
        for u,v in roads:
            degree[u]+=1
            degree[v]+=1
        degree.sort()
        ret=0
        for i in range(len(degree)):
            ret+=(1+i)*degree[i]
        return ret