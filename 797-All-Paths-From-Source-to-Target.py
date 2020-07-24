class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # directed acyclic
        queue=[(0,[0])]
        dest=len(graph)-1
        ret=[]
        while queue:
            target=[]
            for node,path in queue:
                if node==dest:
                    ret.append(path)
                    continue
                next=graph[node]
                if len(next)==0:
                    continue
                elif len(next)==1:
                    path.append(next[0])
                    target.append((next[0],path))
                else:
                    for item in next:
                        tmp=path[:]
                        tmp.append(item)
                        target.append((item,tmp))
            queue=target
        return ret