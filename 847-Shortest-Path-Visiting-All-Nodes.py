import functools
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        mapping=[0]*len(graph)
        mask=1
        full=0
        for i in range(len(graph)):
            mapping[i]=mask
            mask=mask<<1
        full=mask-1
        queue=[(i,0) for i in range(len(graph))]
        step=0
        record={}
        while queue:
            target=[]
            for pos,acc in queue:
                cur=mapping[pos]
                if cur|acc==full:
                    return step
                for idx in graph[pos]:
                    if (idx,acc|cur) not in record:
                        target.append((idx,acc|cur))
                        record[(idx,acc|cur)]=1
            queue=target
            step+=1
        return step