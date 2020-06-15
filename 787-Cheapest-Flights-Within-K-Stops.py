from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src==dst or n<2:
            return 0
        template=[-1]*(K+1)
        record=[template[:] for _ in range(n)]
        record[src][-1]=0
        graph=[[] for _ in range(n)]
        for u,v,w in flights:
            graph[u].append((v,w))
        queue=[src]
        target=[]
        for stop in range(0,K+1):
            for idx in range(len(queue)):
                node=queue[idx]
                dest=graph[node]
                for tgt,w in dest:
                    if record[tgt][stop]<0:
                        record[tgt][stop]=w+record[node][stop-1]
                    else:
                        record[tgt][stop]=min(record[tgt][stop],w+record[node][stop-1])
                    if tgt!=dst and tgt not in target:
                        target.append(tgt)
            queue=target
            target=[]
        ret=-1
        for item in record[dst]:
            if item>=0 and ret<0:
                ret=item
            elif item>=0:
                ret=min(item,ret)
        return ret
        
x=Solution()
print(x.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,2))