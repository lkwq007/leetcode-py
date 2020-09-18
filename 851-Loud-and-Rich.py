class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # richer may be a subset, so it can be treat as edges
        ret=[i for i in range(len(quiet))]
        indegree=[0]*len(quiet)
        graph={}
        for x,y in richer:
            indegree[y]+=1
            if x not in graph:
                graph[x]=[]
            graph[x].append(y)
        queue=[i for i in range(len(quiet)) if indegree[i]==0]
        target=[]
        while queue:
            for idx in queue:
                if idx in graph:
                    for next in graph[idx]:
                        indegree[next]-=1
                        if quiet[ret[idx]]<quiet[ret[next]]:
                            ret[next]=ret[idx]
                        if indegree[next]==0:
                            target.append(next)
            queue=target
            target=[]
        return ret