class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree=[0]
        ret=[0]*(n-1)
        graph=[[] for _ in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ret[0]=n-1
        queue=edges
        record={}
        for i in range(1,n-1):
            target=[]
            while queue:
                cur_queue=[]
                for lst in queue:
                    for u in lst:
                        cnt=0
                        cur_lst=[]
                        for v in graph[u]:
                            if v not in lst:
                                template=lst[:]
                                template.append(v)
                                template.sort()
                                tmp=tuple(template)
                                if tmp not in record:
                                    cnt+=1
                                    record[tmp]=1
                                    cur_lst.append(tmp)
                        if len(cur_lst)>1:
                            cur_queue.append()
            ret[i]=len(target)
            target=[]
        return ret