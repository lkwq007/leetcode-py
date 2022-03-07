class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        queue=[]
        indegree=[0]*n
        graph=[[] for _ in range(n)]
        ret=[[0]*n for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            target=[]
            for item in queue:
                for next in graph[item]:
                    indegree[next]-=1
                    ret[next][item]=1
                    for i in range(n):
                        ret[next][i]=max(ret[next][i],ret[item][i])
                    if indegree[next]==0:
                        target.append(next)
            queue=target
        # print(ret)
        return [[i for i in range(len(lst)) if lst[i]>0] for lst in ret]