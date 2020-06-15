from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph_in={}
        graph_out={}
        for a,b in connections:
            if b in graph_in:
                graph_in[b].append(a)
            else:
                graph_in[b]=[a]
            if a in graph_out:
                graph_out[a].append(b)
            else:
                graph_out[a]=[b]
        queue=[0]
        idx=0
        cnt=0
        record=[0]*n
        while idx<len(queue):
            node=queue[idx]
            record[node]=1
            idx+=1
            if node in graph_out:
                for item in graph_out[node]:
                    if record[item]==0:
                        cnt+=1
                        queue.append(item)
            if node in graph_in:
                for item in graph_in[node]:
                    if record[item]==0:
                        queue.append(item)
        return cnt
x=Solution()
print(x.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]]))